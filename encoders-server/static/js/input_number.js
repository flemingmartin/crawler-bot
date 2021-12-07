(function() {
 
  window.inputNumber = function(el) {
    el.each(function() {
      init($(this));
    });

    function init(el) {
      var min = el.attr('min');
      var max = el.attr('max');
      var step = parseFloat(el.attr('step'));
      var presicion = Math.log10(step)*-1

      var els = {};
      els.dec = el.prev();
      els.inc = el.next();

      els.dec.on('click', decrement);
      els.inc.on('click', increment);

      function decrement() {
        var value = parseFloat(el[0].value);
        var new_value = value-step;
        if (new_value > min){
          el[0].value = new_value.toFixed(presicion);
        }
        
      }

      function increment() {
        var value = parseFloat(el[0].value);
        var new_value = value+step;
        if (new_value < max){
          el[0].value = new_value.toFixed(presicion);
        }
      }
    }
  }
})();

inputNumber($('.input-number'));