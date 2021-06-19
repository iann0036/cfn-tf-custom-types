# TF::AVI::Virtualservice ClientLogFiltersDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allheaders" title="AllHeaders">AllHeaders</a>" : <i>Boolean</i>,
    "<a href="#duration" title="Duration">Duration</a>" : <i>Double</i>,
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#index" title="Index">Index</a>" : <i>Double</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#clientip" title="ClientIp">ClientIp</a>" : <i>[ <a href="clientipdefinition.md">ClientIpDefinition</a>, ... ]</i>,
    "<a href="#uri" title="Uri">Uri</a>" : <i>[ <a href="uridefinition.md">UriDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#allheaders" title="AllHeaders">AllHeaders</a>: <i>Boolean</i>
<a href="#duration" title="Duration">Duration</a>: <i>Double</i>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#index" title="Index">Index</a>: <i>Double</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#clientip" title="ClientIp">ClientIp</a>: <i>
      - <a href="clientipdefinition.md">ClientIpDefinition</a></i>
<a href="#uri" title="Uri">Uri</a>: <i>
      - <a href="uridefinition.md">UriDefinition</a></i>
</pre>

## Properties

#### AllHeaders

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Duration

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Index

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientIp

_Required_: No

_Type_: List of <a href="clientipdefinition.md">ClientIpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uri

_Required_: No

_Type_: List of <a href="uridefinition.md">UriDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

