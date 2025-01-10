 // 假設從後端獲取的資料
    // const bookedSeats = [
    //     { row: "A", col: 1 },
    //     { row: "A", col: 4 },
    //     { row: "B", col: 1 },
    //     { row: "B", col: 4 }
    // ];
let bookedSeats = []; // 全局變數，存儲座位資訊

document.getElementById('showtime').addEventListener('change', function () {
const showtimeSelect = document.getElementById('showtime');
const selectedOption = showtimeSelect.options[showtimeSelect.selectedIndex];
const showId = selectedOption.value; // 獲取 show_id

console.log("Selected Option:", selectedOption); // 調試選中項
console.log("Show ID:", showId); // 調試 show_id

if (showId) {
    fetch(`/api/seats/${showId}/`)
        .then(response => response.json())
        .then(data => {
            // 清空全局 bookedSeats，然後加入新的數據
            bookedSeats = data.booked_seats;

            console.log("Updated Booked Seats:", bookedSeats);
            plan_seat();

        })
        .catch(error => {
            console.error('Error fetching seats:', error);
        });
}
})



                            //第一部分消失 顯示第二部分(座位)
const contactDiv = document.getElementById('contact1');
const seatSelectionDiv = document.getElementById('contact2');

function plan_seat(){
    const seatContainer = document.getElementById('seat-container');

    // 確保 seatContainer 存在
    if (!seatContainer) {
        console.error('Seat container not found!');
        return;
    }

    // 清空座位容器的內容
    seatContainer.innerHTML = '';


    // 定義行與列
    const rows = ["A", "B", "C", "D", "E", "F"];
    const cols = 5;
    //const seatContainer = document.getElementById('seat-container');
    const seatInput = document.getElementById('seat');

    let selectedSeat = null; // 當前選中的座位

    rows.forEach(row => {
        for (let col = 1; col <= cols; col++) {
            const seatId = `${row}${col}`;
            const seatElement = document.createElement('div');
            seatElement.classList.add('seat');
            seatElement.textContent = seatId;

            // 判斷是否已被預訂
            if (bookedSeats.some(seat => seat.row === row && seat.col === col)) {
                seatElement.classList.add('booked');
            } else {
                // 點擊事件：選擇座位
                seatElement.addEventListener('click', () => {
                    if (selectedSeat) {
                        selectedSeat.classList.remove('selected'); // 取消之前的選中狀態
                    }
                    selectedSeat = seatElement;
                    selectedSeat.classList.add('selected'); // 添加選中樣式
                    seatInput.value = seatId; // 更新選中的座位到輸入框
                });
            }

            seatContainer.appendChild(seatElement);
        }
    });
}

submitButton1.addEventListener('click', () => {
    const showtimeSelect = document.getElementById('showtime');
    const selectedShowtimeOption = showtimeSelect.options[showtimeSelect.selectedIndex];

    // 確保有選中的場次
    const showId = selectedShowtimeOption?.value;

    if (!showId) {
        alert('未選擇有效的場次！');
        return;
    }

    console.log('提交的場次 ID:', showId);

    // 自動載入座位
    fetch(`/api/seats/${showId}/`)
        .then(response => response.json())
        .then(data => {
            bookedSeats = data.booked_seats; // 更新全局變數
            console.log('返回的座位資料:', bookedSeats);
            plan_seat(); // 呼叫座位渲染函數
        })
        .catch(error => {
            console.error('座位表格載入失敗:', error);
        });

    // 切換到座位選擇畫面
    const contactDiv = document.getElementById('contact1');
    const seatSelectionDiv = document.getElementById('contact2');
    contactDiv.classList.add('hidden');
    seatSelectionDiv.classList.remove('hidden');
    seatSelectionDiv.classList.add('tm-section');
});


document.getElementById('submit-button-2').addEventListener('click', () => {
    const seatInput = document.getElementById('seat').value;
    const nameInput = document.getElementById('name').value;
    const phoneInput = document.getElementById('phonenum').value;
    const showtimeSelect = document.getElementById('showtime');
    const selectedShowtimeOption = showtimeSelect.options[showtimeSelect.selectedIndex];

    const showId = selectedShowtimeOption?.value; // 場次 ID

    if (!seatInput || !nameInput || !phoneInput || !showId) {
        alert('請輸入完整的資料！');
        return;
    }

    const [seatRow, seatCol] = [seatInput.slice(0, 1), seatInput.slice(1)]; // 提取座位行和列

    console.log({
        phone: phoneInput,
        name: nameInput,
        show_id: showId,
        seat_row: seatRow,
        seat_col: seatCol
    });
    

    // 發送資料到後端
    fetch('/api/submit_ticket/', {
    method: 'POST',
    body: new URLSearchParams({
        phone: phoneInput,
        name: nameInput,
        show_id: showId,
        seat_row: seatRow,
        seat_col: seatCol
    })
})
.then(response => {
    if (!response.ok) {
        return response.json().then(errorData => {
            throw new Error(errorData.error || '提交失敗，請稍後再試！');
        });
    }
    return response.json();
})
.then(data => {
    if (data.success) {
        Swal.fire({
            title: '訂單確認',
            html: `
                <p>已成功預訂座位 <b style="color: green;">${seatInput}</b>，姓名：<b>${nameInput}</b>。</p>
                <p>隨機驗證碼：<span style="color: red; font-size: 1.5em; font-weight: bold;">${data.verify_code}</span></p>
            `,
            icon: 'success',
            confirmButtonText: '確定'
        }).then(() => {
            window.location.href = `/search_order/?query=${phoneInput}`;
        });
    } else {
        throw new Error(data.error || '提交失敗，請稍後再試！');
    }
})
.catch(error => {
    console.error('提交失敗:', error.message);
    
    // 處理特定錯誤訊息
    if (error.message.includes('電話號碼必須為 9 位數字')) {
        Swal.fire({
            title: '錯誤',
            text: '電話號碼必須為 9 位數字，請重新輸入！',
            icon: 'error',
            confirmButtonText: '確定'
        });
    } else {
        Swal.fire({
            title: '錯誤',
            text: error.message || '提交失敗，請稍後再試！',
            icon: 'error',
            confirmButtonText: '確定'
        });
    }
});

});

