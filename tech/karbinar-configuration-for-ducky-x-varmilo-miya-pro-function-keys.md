Title: Karbinar Configuration for Ducky X Varmilo Miya Pro function keys
Date: 2021-04-22 22:32
Category: Tech
Lang: en
Slug: karbinar-configuration-for-ducky-x-varmilo-miya-pro-function-keys

My current keyboard is a [Ducky X Varmilo Miya Pro](https://mechanicalkeyboards.com/shop/index.php?l=product_detail&p=4285). This keyboard gets stellar reviews from multiple mechanical keyboard Youtube channels. It is pleasant to use and aesthetically appealing, perfect to be paired with a Magic Trackpad.

The only annoying thing I have using this board is that the function keys are integrated with the number keys and you have to switch mode to toggle between the two. Usually my intuition is to use Fn+Number keys to trigger  functionalities such as volume increase/decrease. But for Miya Pro, you have to use Fn+pageDn to switch into the function mode, then press "-"/F11 to decrease the volume. For typing numbers you’ll have to press Fn+pageUp to switch back. While there is a light on either pageUp or pageDown to indicate which mode you're in, it is very often you forgot it's in the function mode when trying to type numbers.

Now you can use a [Karabiner-Elements](https://karabiner-elements.pqrs.org/) config to solve this. Download the Karabiner Elements complex modifications config [here](https://ke-complex-modifications.pqrs.org/#fn_plus_numbers_to_function_keys) then Add the Rule "Map fn + number keys to their corresponding media control keys (rev 2)". Then you can use Fn+Number keys, without ever switch the mode again.

Happy typing.
