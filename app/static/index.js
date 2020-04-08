var app = new Vue({
  el: '#app',
  data: {
    discountCode: '',
    products: [],
    cart: {
        code: '',
        elements: [],
        discounts: []
    },
    checkoutData: {
        active: false,
    }
  },
  computed: {
    totalPrice: function() {
        totalCost = 0;
        this.cart.elements.forEach((element) => {
            totalCost += element.product.price;
        });

        this.cart.discounts.forEach((discount) => {
            totalCost -= totalCost * (discount.percentage * 0.0001);
        });
        return totalCost * 0.01
    },
    totalPriceWithoutDiscount: function() {
        totalCost = 0;
        this.cart.elements.forEach((element) => {
            totalCost += element.product.price;
        });

        return totalCost * 0.01
    },
    totalPriceWithoutDiscountClass: function() {
        return {
            'cart-total__discounted': this.hasDiscount()
        }
    }
  },
  methods: {
    discountCodeError: function() {
        return this.cart.error && this.cart.error.code;
    },
    hasDiscount: function() {
        return Array.isArray(this.cart.discounts) && this.cart.discounts.length
    },
    isCheckedOut: function() {
        return this.checkoutData && this.checkoutData.active;
    },

    orderHasDiscounts: function() {
        return this.checkoutData &&  Array.isArray(this.checkoutData.discounts) && this.checkoutData.discounts.length
    },
    getCart: function(cartCode) {
        if (!cartCode) {
            this.createNewCart();
        } else {
            axios.get('/cart/' + cartCode).then(({data}) => {
                this.cart = data;
            })
        }
    },
    createNewCart: function() {
       axios.post('/cart').then(({data}) => {
            this.cart = data;
            localStorage.setItem('cartCode', data.code);
       });
    },
    addNewItem: function(reference) {
        axios.post('/cart/' + this.cart.code, {reference}).then(({data}) => {
            this.cart = data;
        });
    },
    addNewDiscount: function() {
        axios.post('/cart/' + this.cart.code + '/discount/' + this.discountCode).then(({data}) => {
            this.cart = data;
            this.discountCode = '';
        });
    },
    removeItem: function(code) {
        axios.delete('/cart/' + this.cart.code + '/' + code).then(({data}) => {
            this.cart = data;
        });
    },
    checkout: function() {
        axios.get('/cart/' + this.cart.code + '/checkout').then(({data}) => {
            axios.get('/order/' + data.code).then(({data}) => {
                data.active = true;
                this.checkoutData = data;
                this.createNewCart();
            });

        })
    }
  },
  mounted: function(){
    axios.get('/product').then(({data}) => {
        this.products = data['products'];
    });

    let code = localStorage.getItem('cartCode');
    this.getCart(code);
  },
  delimiters: ['[[',']]']
})