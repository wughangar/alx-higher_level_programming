$(document).ready(function() {
	function fetchAndDisplayTranslation() {
		const languageCode = $("#language_code").val();
		const apiUrl = "https://www.fourtonfish.com/hellosalut/hello/?lang=" + languageCode;

		$.get(apiUrl, function(data) {
			$("#hello").text(data.hello);
		});
	});
$("#btn_translate").click(fetchAndDisplayTranslation);
$("#language_code").keypress(function(event) {
	 if (event.which === 13) {
		 fetchAndDisplayTranslation();
	 }
});
});
