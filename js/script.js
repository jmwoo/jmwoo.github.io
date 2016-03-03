$(function () {
	console.log('hello world!');

	// make progress bar 'great again'
	var $progressBar = $('#progress-bar');

	var i = 1;
	var interval = setInterval(function () {
		var percentageStr = i.toString();
		$progressBar.attr('aria-valuenow', percentageStr);
		$progressBar.css({'width': percentageStr + '%'});
		$progressBar.text(percentageStr + '%');
		i++;
		if (i === 101) {
			clearInterval(interval);
			$('.coming-to-life').hide('slow');
			$('.is-alive').show('slow');
		}
	}, 50 * 1);
});