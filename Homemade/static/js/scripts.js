document.addEventListener('DOMContentLoaded', function() {
    console.log('The website template is ready!');

    // Example of populating the services table in owner dashboard
    if (document.querySelector('#services-table')) {
        $('#services-table').DataTable({
            data: [
                [1, 'Custom Paintings', 'Personalized paintings crafted by skilled artists.', '$50', '<button class="btn btn-sm btn-primary">Edit</button> <button class="btn btn-sm btn-danger">Delete</button>'],
                [2, 'Handmade Candles', 'Scented and decorative handmade candles.', '$20', '<button class="btn btn-sm btn-primary">Edit</button> <button class="btn btn-sm btn-danger">Delete</button>']
            ],
            columns: [
                { title: "ID" },
                { title: "Service Name" },
                { title: "Description" },
                { title: "Price" },
                { title: "Actions" }
            ]
        });
    }

    // Example of populating the orders table in owner dashboard
    if (document.querySelector('#orders-table')) {
        $('#orders-table').DataTable({
            data: [
                [101, 'John Doe', 'Custom Paintings', 'Pending', '<button class="btn btn-sm btn-primary">View</button> <button class="btn btn-sm btn-danger">Cancel</button>'],
                [102, 'Jane Smith', 'Handmade Candles', 'Completed', '<button class="btn btn-sm btn-primary">View</button> <button class="btn btn-sm btn-danger">Cancel</button>']
            ],
            columns: [
                { title: "Order ID" },
                { title: "Customer Name" },
                { title: "Service" },
                { title: "Status" },
                { title: "Actions" }
            ]
        });
    }

    // Example of populating the available services table in user dashboard
    if (document.querySelector('#available-services-table')) {
        $('#available-services-table').DataTable({
            data: [
                [1, 'Custom Paintings', 'Personalized paintings crafted by skilled artists.', '$50', '<button class="btn btn-sm btn-primary">Order</button>'],
                [2, 'Handmade Candles', 'Scented and decorative handmade candles.', '$20', '<button class="btn btn-sm btn-primary">Order</button>']
            ],
            columns: [
                { title: "ID" },
                { title: "Service Name" },
                { title: "Description" },
                { title: "Price" },
                { title: "Actions" }
            ]
        });
    }

    // Example of populating the user orders table in user dashboard
    if (document.querySelector('#user-orders-table')) {
        $('#user-orders-table').DataTable({
            data: [
                [101, 'Custom Paintings', 'Pending', '<button class="btn btn-sm btn-primary">View</button> <button class="btn btn-sm btn-danger">Cancel</button>'],
                [102, 'Handmade Candles', 'Completed', '<button class="btn btn-sm btn-primary">View</button> <button class="btn btn-sm btn-danger">Cancel</button>']
            ],
            columns: [
                { title: "Order ID" },
                { title: "Service" },
                { title: "Status" },
                { title: "Actions" }
            ]
        });
    }
});