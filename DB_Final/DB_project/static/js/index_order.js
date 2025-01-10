
// 更新電影圖片
function updateImage() {
    const select = document.getElementById('movies');
    const image = document.getElementById('movie-image');
    image.src = select.value; // 根據選擇更新圖片路徑
}


// 更新分店
function updateBranch(movieId) {
    const branchSelect = document.getElementById('branch');
    const showtimeSelect = document.getElementById('showtime');
    branchSelect.innerHTML = '<option value="">載入中...</option>'; // 初始顯示載入中

    fetch(`/api/branches/${movieId}/`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(branches => {
            branchSelect.innerHTML = ''; // 清空選單
            if (branches.length > 0) {
                branches.forEach((branch, index) => {
                    const option = document.createElement('option');
                    option.value = branch;
                    option.textContent = branch;
                    branchSelect.appendChild(option);

                    // 預設選中第一個有效選項
                    if (index === 0) {
                        branchSelect.selectedIndex = 0;
                    }
                });

                // 自動加載第一個分店的場次
                const firstBranch = branches[0];
                updateShowtime(movieId, firstBranch);
            } else {
                branchSelect.innerHTML = '<option value="">無可用分店</option>';
                showtimeSelect.innerHTML = '<option value="">無可用場次</option>';
            }
        })
        .catch(error => {
            console.error('Error fetching branches:', error);
            branchSelect.innerHTML = '<option value="">載入失敗，請重試</option>';
            showtimeSelect.innerHTML = '<option value="">無可用場次</option>';
        });
}

function updateShowtime(movieId, branch) {
    const showtimeSelect = document.getElementById('showtime');
    showtimeSelect.innerHTML = '<option value="">載入中...</option>'; // 初始顯示載入中

    fetch(`/api/showtimes/${movieId}/${encodeURIComponent(branch)}/`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(showtimes => {
            showtimeSelect.innerHTML = ''; // 清空場次選單
            if (showtimes.length > 0) {
                showtimes.forEach((showtime, index) => {
                    const option = document.createElement('option');
                    option.value = showtime.show_id; // 使用 show_id 作為值
                    option.textContent = showtime.show_time; // 顯示格式化的場次時間
                    showtimeSelect.appendChild(option);

                    // 預設選中第一個有效場次
                    if (index === 0) {
                        showtimeSelect.selectedIndex = 0;
                    }
                });

                console.log('預設選中的場次 ID:', showtimeSelect.options[0].value);
            } else {
                showtimeSelect.innerHTML = '<option value="">無可用場次</option>';
            }
        })
        .catch(error => {
            console.error('Error fetching showtimes:', error);
            showtimeSelect.innerHTML = '<option value="">載入失敗，請重試</option>';
        });
}




// 如果換了movie 則更新分店資訊
document.getElementById('movies').addEventListener('change', function () {
    const selectedOption = this.options[this.selectedIndex];
    const movieId = selectedOption.getAttribute('id');
    updateBranch(movieId);
});

// 場次選擇
document.getElementById('branch').addEventListener('change', function () {
    const movieSelect = document.getElementById('movies');
    const branchSelect = document.getElementById('branch');

    const selectedMovieOption = movieSelect.options[movieSelect.selectedIndex];
    const selectedBranchOption = branchSelect.options[branchSelect.selectedIndex];

    const movieId = selectedMovieOption?.getAttribute('id'); // 獲取 movie_id
    const branch = selectedBranchOption?.value; // 獲取分店

    if (movieId && branch) {
        updateShowtime(movieId, branch); // 更新場次
    }
});



window.onload = function () {
    const urlParams = new URLSearchParams(window.location.hash.split('?')[1]); // 獲取 URL 中的參數
    const movieId = urlParams.get('movie_id'); // 獲取 movie_id
    const moviesSelect = document.getElementById('movies');
    const movieImage = document.getElementById('movie-image');

    if (movieId) {
        // 如果 URL 中包含 movie_id，則根據該 ID 預選電影
        let movieFound = false;
        for (let i = 0; i < moviesSelect.options.length; i++) {
            if (moviesSelect.options[i].id === movieId) {
                moviesSelect.selectedIndex = i;
                movieImage.src = moviesSelect.options[i].value; // 更新電影圖片
                movieFound = true;
                break;
            }
        }

        if (movieFound) {
            moviesSelect.dispatchEvent(new Event('change')); // 觸發分店和場次更新
        } else {
            console.error('URL 中的 movie_id 不匹配任何電影選項');
        }
    } else {
        // 如果 URL 中沒有 movie_id，則執行原邏輯，預設選擇第一部電影
        const firstMovieOption = moviesSelect.options[moviesSelect.selectedIndex];
        const firstMovieId = firstMovieOption?.getAttribute('id'); // 確保存在 movieId

        if (firstMovieId) {
            updateBranch(firstMovieId); // 初始加載分店，並自動更新第一個分店的場次
        } else {
            console.error('無法找到有效的電影選項！');
        }
    }
};


function selectMovie(movieId, movieImg) {
    // 更新電影下拉選單
    const movieSelect = document.getElementById('movies');
    for (let i = 0; i < movieSelect.options.length; i++) {
        if (movieSelect.options[i].id === movieId) {
            movieSelect.selectedIndex = i; // 選中正確的電影
            break;
        }
    }

    // 更新電影圖片
    const movieImage = document.getElementById('movie-image');
    movieImage.src = movieImg;

    // 模擬選單改變事件，觸發後續更新（如分店和場次）
    movieSelect.dispatchEvent(new Event('change'));

    // 跳轉快速訂票區域
    window.location.href = `#order?movie_id=${movieId}`;
}




document.getElementById('movies').addEventListener('change', function () {
    const selectedOption = this.options[this.selectedIndex];
    const movieId = selectedOption.getAttribute('id');
    updateBranch(movieId);
});

function validatePhoneNumber(input) {
    const phoneError = document.getElementById('phone-error');
    const phone = input.value;

    if (phone.length === 9 && /^\d{9}$/.test(phone)) {
        phoneError.style.display = 'none'; // 隱藏錯誤提示
        input.setCustomValidity(''); // 清除 HTML5 驗證錯誤
    } else {
        phoneError.style.display = 'block'; // 顯示錯誤提示
        input.setCustomValidity('電話號碼必須為 9 位數字。');
    }
}

function checkPhoneNumber(input) {
    const phone = input.value;
    const nameInput = document.getElementById('name');

    if (phone.length === 9 && /^\d{9}$/.test(phone)) {
        fetch(`/api/check_phone/?phone=${phone}`)
            .then(response => response.json())
            .then(data => {
                if (data.exists) {
                    nameInput.value = data.name; // 填入名字
                    nameInput.setAttribute('readonly', true); // 設置為不可修改
                } else {
                    nameInput.value = ''; // 清空名字
                    nameInput.removeAttribute('readonly'); // 恢復可編輯
                }
            })
            .catch(error => {
                console.error('檢查電話號碼失敗:', error);
            });
    } else {
        nameInput.value = ''; // 清空名字
        nameInput.removeAttribute('readonly'); // 恢復可編輯
    }
}


// 宣告按鈕1和按鈕2
const submitButton2 = document.getElementById('submit-button-2');
const submitButton1 = document.getElementById('submit-button-1');