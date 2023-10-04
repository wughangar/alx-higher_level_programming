const apiUrl = "https://fourtonfish.com/hellosalut/?lang=fr";

$.get(apiUrl, function(data) {
	const translation = data.hello;
	$("#hello").text(translation);
});
