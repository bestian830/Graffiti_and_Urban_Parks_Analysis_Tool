"""
Shichao Tian
Relationship of parks and graffiti analysis. --- Final Project
Uncomment is the Gui version
Comment part is the command line version
"""
from utils.functions import (data_get, menu, option, park_option, invalid,
                             graff_option, get_review, ask_km, back_menu,
                             appreciate, back)
from models.graffiti import Graffiti
from models.park import Park
from utils.create_instances import (create_park_instances,
                                    create_graffiti_instances)
from Views.visualization import (plot_park_counts,
                                 plot_graffiti_counts,
                                 plot_graffitis_near_parks)
import requests

LOOP_CORRECT = 1
LOOP_OUT = 0


def main():
    # Show the initial menu
    menu()

    # Enter the main program loop
    FLAG = LOOP_CORRECT
    while FLAG == LOOP_CORRECT:
        try:
            # Get user's option
            user_option = option()

            try:
                # Fetch and prepare data
                parks, graffs = data_get()
            except requests.HTTPError as e:
                print(f"Failed to download data: {e}")
            except ValueError as e:
                print(f"Data parsing error: {e}")
            except KeyError as e:
                print(f"Data cleaning error, missing expected key: {e}")

            if user_option in ['p', 'park']:
                # Handle park data
                parks_instances = create_park_instances(parks)
                park_count = Park.park_in_neighbour(parks_instances)
                plot_park_counts(park_count)

                further_option = graff_option()
                if further_option == 'y':
                    km = ask_km()
                    graffiti_instances = create_graffiti_instances(graffs)
                    plot_graffitis_near_parks(
                        parks_instances, graffiti_instances, km)
                    back()
                elif further_option == 'n':
                    back_menu()
                else:
                    invalid()

            elif user_option in ['g', 'graffiti']:
                # Handle graffiti data
                graffiti_instances = create_graffiti_instances(graffs)
                graff_count = Graffiti.graffiti_in_neighbour(
                    graffiti_instances)
                plot_graffiti_counts(graff_count)

                further_option = park_option()
                if further_option == 'y':
                    km = ask_km()
                    parks_instances = create_park_instances(parks)
                    plot_graffitis_near_parks(
                        parks_instances, graffiti_instances, km)
                    back()
                elif further_option == 'n':
                    back_menu()
                else:
                    invalid()

            elif user_option in ['q', 'quit']:
                FLAG = LOOP_OUT
                review = get_review()
                print(f"User review: {review}")
                appreciate()

            else:
                invalid()

        except ValueError as e:
            print(e)
        except Exception as e:
            print(f"Error during processing: {e}")


if __name__ == "__main__":
    main()
