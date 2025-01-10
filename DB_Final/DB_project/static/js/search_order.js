function cancelOrder(phone, verifyCode) {
    if (confirm("您確定要取消訂單嗎？")) {
        fetch('/cancel_order/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': getCookie('csrftoken') // 確保 CSRF 驗證
            },
            body: new URLSearchParams({
                phone: phone,
                verify_code: verifyCode
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('訂單已成功取消！');
                // 改為重新加載當前頁面
                window.location.reload();
            } else {
                alert('取消失敗：' + data.error);
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('取消失敗，請稍後再試！');
        });
    }
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

