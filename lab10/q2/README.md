To register a new commuter in the database - localhost:<port number>/zayacab/user/register and pass username and password in POST request parameters.

To register new driver in the database - localhost:<port number>/zayacab/driver/register and pass username and password in POST request parameters and none for GET request

To get user trip history - localhost:<port number>/zayacab/<commuter_id>/history

To get user trip history - localhost:<port number>/zayacab/<driver_id>/history

To get the user location - localhost:<port number>/zayacab/user/location/<commuter_id>

To change the status of a driver after booking and completion of a trip - localhost:<port number>/zayacab/update/<driver_id> and pass status params in POST request.

To book a cab - localhost:<port number>/zayacab/<commuter_id>/<driver_id> and pass source, destination and fare in POST request.

Get the list of all available drivers- localhost:<port number>/zayacab/driver/available