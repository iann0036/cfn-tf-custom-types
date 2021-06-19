# TF::AzureRM::StorageAccount RoutingDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#choice" title="Choice">Choice</a>" : <i>String</i>,
    "<a href="#publishinternetendpoints" title="PublishInternetEndpoints">PublishInternetEndpoints</a>" : <i>Boolean</i>,
    "<a href="#publishmicrosoftendpoints" title="PublishMicrosoftEndpoints">PublishMicrosoftEndpoints</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#choice" title="Choice">Choice</a>: <i>String</i>
<a href="#publishinternetendpoints" title="PublishInternetEndpoints">PublishInternetEndpoints</a>: <i>Boolean</i>
<a href="#publishmicrosoftendpoints" title="PublishMicrosoftEndpoints">PublishMicrosoftEndpoints</a>: <i>Boolean</i>
</pre>

## Properties

#### Choice

Specifies the kind of network routing opted by the user. Possible values are `InternetRouting` and `MicrosoftRouting`. Defaults to `MicrosoftRouting`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublishInternetEndpoints

Should internet routing storage endpoints be published? Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublishMicrosoftEndpoints

Should microsoft routing storage endpoints be published? Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

