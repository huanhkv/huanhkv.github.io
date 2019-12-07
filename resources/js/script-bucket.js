var bucket_list = [
	{checked : 1, content : "Viết blog cá nhân"},
	{checked : 0, content : "Có bằng master"},
	{checked : 0, content : "Có bằng PhD"},
	{checked : 0, content : "Đạt lương 12tr/tháng"},
	{checked : 0, content : "Đạt lương 20tr/tháng"},
	{checked : 0, content : "Đạt lương 25tr/tháng"},
	{checked : 0, content : "Đạt lương 30tr/tháng"},
	{checked : 0, content : "Đạt lương 40tr/tháng"},
	{checked : 0, content : "Tham quan Stanford University"},
	{checked : 0, content : "Đưa ba mẹ đi chơi trong nước"},
	{checked : 0, content : "Đưa ba mẹ đi chơi ngoài nước"},
	{checked : 0, content : "Cưới vợ"},
	{checked : 0, content : "Sống thử ở Nhật Bản"},
	{checked : 0, content : "Sống thử ở Thụy Sĩ"},
	{checked : 0, content : "Kiếm tiền xây nhà"}
];

//{checked : 0, content : ""},

checked = ['✗', '✓']

$.each(bucket_list, function(index, value){
	var temp = "<li>"+ checked[value.checked] + " " + value.content + "</li>"
	$(".show-bucket-list").append(temp)
})
