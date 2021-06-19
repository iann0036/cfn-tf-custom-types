# TF::FortiOS::WebproxyProfile

Configure web proxy profiles.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::WebproxyProfile",
    "Properties" : {
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#headerclientip" title="HeaderClientIp">HeaderClientIp</a>" : <i>String</i>,
        "<a href="#headerfrontendhttps" title="HeaderFrontEndHttps">HeaderFrontEndHttps</a>" : <i>String</i>,
        "<a href="#headerviarequest" title="HeaderViaRequest">HeaderViaRequest</a>" : <i>String</i>,
        "<a href="#headerviaresponse" title="HeaderViaResponse">HeaderViaResponse</a>" : <i>String</i>,
        "<a href="#headerxauthenticatedgroups" title="HeaderXAuthenticatedGroups">HeaderXAuthenticatedGroups</a>" : <i>String</i>,
        "<a href="#headerxauthenticateduser" title="HeaderXAuthenticatedUser">HeaderXAuthenticatedUser</a>" : <i>String</i>,
        "<a href="#headerxforwardedfor" title="HeaderXForwardedFor">HeaderXForwardedFor</a>" : <i>String</i>,
        "<a href="#logheaderchange" title="LogHeaderChange">LogHeaderChange</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#stripencoding" title="StripEncoding">StripEncoding</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#headers" title="Headers">Headers</a>" : <i>[ <a href="headersdefinition.md">HeadersDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::WebproxyProfile
Properties:
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#headerclientip" title="HeaderClientIp">HeaderClientIp</a>: <i>String</i>
    <a href="#headerfrontendhttps" title="HeaderFrontEndHttps">HeaderFrontEndHttps</a>: <i>String</i>
    <a href="#headerviarequest" title="HeaderViaRequest">HeaderViaRequest</a>: <i>String</i>
    <a href="#headerviaresponse" title="HeaderViaResponse">HeaderViaResponse</a>: <i>String</i>
    <a href="#headerxauthenticatedgroups" title="HeaderXAuthenticatedGroups">HeaderXAuthenticatedGroups</a>: <i>String</i>
    <a href="#headerxauthenticateduser" title="HeaderXAuthenticatedUser">HeaderXAuthenticatedUser</a>: <i>String</i>
    <a href="#headerxforwardedfor" title="HeaderXForwardedFor">HeaderXForwardedFor</a>: <i>String</i>
    <a href="#logheaderchange" title="LogHeaderChange">LogHeaderChange</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#stripencoding" title="StripEncoding">StripEncoding</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#headers" title="Headers">Headers</a>: <i>
      - <a href="headersdefinition.md">HeadersDefinition</a></i>
</pre>

## Properties

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeaderClientIp

Action to take on the HTTP client-IP header in forwarded requests: forwards (pass), adds, or removes the HTTP header. Valid values: `pass`, `add`, `remove`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeaderFrontEndHttps

Action to take on the HTTP front-end-HTTPS header in forwarded requests: forwards (pass), adds, or removes the HTTP header. Valid values: `pass`, `add`, `remove`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeaderViaRequest

Action to take on the HTTP via header in forwarded requests: forwards (pass), adds, or removes the HTTP header. Valid values: `pass`, `add`, `remove`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeaderViaResponse

Action to take on the HTTP via header in forwarded responses: forwards (pass), adds, or removes the HTTP header. Valid values: `pass`, `add`, `remove`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeaderXAuthenticatedGroups

Action to take on the HTTP x-authenticated-groups header in forwarded requests: forwards (pass), adds, or removes the HTTP header. Valid values: `pass`, `add`, `remove`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeaderXAuthenticatedUser

Action to take on the HTTP x-authenticated-user header in forwarded requests: forwards (pass), adds, or removes the HTTP header. Valid values: `pass`, `add`, `remove`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeaderXForwardedFor

Action to take on the HTTP x-forwarded-for header in forwarded requests: forwards (pass), adds, or removes the HTTP header. Valid values: `pass`, `add`, `remove`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogHeaderChange

Enable/disable logging HTTP header changes. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Profile name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StripEncoding

Enable/disable stripping unsupported encoding from the request header. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Headers

_Required_: No

_Type_: List of <a href="headersdefinition.md">HeadersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

