# TF::FortiOS::WebproxyProfile HeadersDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#action" title="Action">Action</a>" : <i>String</i>,
    "<a href="#addoption" title="AddOption">AddOption</a>" : <i>String</i>,
    "<a href="#base64encoding" title="Base64Encoding">Base64Encoding</a>" : <i>String</i>,
    "<a href="#content" title="Content">Content</a>" : <i>String</i>,
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
    "<a href="#dstaddr" title="Dstaddr">Dstaddr</a>" : <i>[ <a href="dstaddrdefinition.md">DstaddrDefinition</a>, ... ]</i>,
    "<a href="#dstaddr6" title="Dstaddr6">Dstaddr6</a>" : <i>[ <a href="dstaddr6definition.md">Dstaddr6Definition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#action" title="Action">Action</a>: <i>String</i>
<a href="#addoption" title="AddOption">AddOption</a>: <i>String</i>
<a href="#base64encoding" title="Base64Encoding">Base64Encoding</a>: <i>String</i>
<a href="#content" title="Content">Content</a>: <i>String</i>
<a href="#id" title="Id">Id</a>: <i>Double</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
<a href="#dstaddr" title="Dstaddr">Dstaddr</a>: <i>
      - <a href="dstaddrdefinition.md">DstaddrDefinition</a></i>
<a href="#dstaddr6" title="Dstaddr6">Dstaddr6</a>: <i>
      - <a href="dstaddr6definition.md">Dstaddr6Definition</a></i>
</pre>

## Properties

#### Action

Action when the HTTP header is forwarded. Valid values: `add-to-request`, `add-to-response`, `remove-from-request`, `remove-from-response`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AddOption

Configure options to append content to existing HTTP header or add new HTTP header. Valid values: `append`, `new-on-not-found`, `new`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Base64Encoding

Enable/disable use of base64 encoding of HTTP content. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Content

HTTP header content.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

HTTP forwarded header id.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

HTTP forwarded header name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

Configure protocol(s) to take add-option action on (HTTP, HTTPS, or both). Valid values: `https`, `http`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dstaddr

_Required_: No

_Type_: List of <a href="dstaddrdefinition.md">DstaddrDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dstaddr6

_Required_: No

_Type_: List of <a href="dstaddr6definition.md">Dstaddr6Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

