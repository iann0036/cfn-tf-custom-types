# TF::Okta::InlineHook

Creates an inline hook.

This resource allows you to create and configure an inline hook.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Okta::InlineHook",
    "Properties" : {
        "<a href="#auth" title="Auth">Auth</a>" : <i>[ <a href="authdefinition.md">AuthDefinition</a>, ... ]</i>,
        "<a href="#channel" title="Channel">Channel</a>" : <i>[ <a href="channeldefinition.md">ChannelDefinition</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#version" title="Version">Version</a>" : <i>String</i>,
        "<a href="#headers" title="Headers">Headers</a>" : <i>[ <a href="headersdefinition.md">HeadersDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Okta::InlineHook
Properties:
    <a href="#auth" title="Auth">Auth</a>: <i>
      - <a href="authdefinition.md">AuthDefinition</a></i>
    <a href="#channel" title="Channel">Channel</a>: <i>
      - <a href="channeldefinition.md">ChannelDefinition</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#version" title="Version">Version</a>: <i>String</i>
    <a href="#headers" title="Headers">Headers</a>: <i>
      - <a href="headersdefinition.md">HeadersDefinition</a></i>
</pre>

## Properties

#### Auth

Authentication required for inline hook request.

_Required_: No

_Type_: List of <a href="authdefinition.md">AuthDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Channel

Details of the endpoint the inline hook will hit.
- `version` - (Required) Version of the channel. The currently-supported version is `"1.0.0"`.
- `uri` - (Required) The URI the hook will hit.
- `type` - (Optional) The type of hook to trigger. Currently, the only supported type is `"HTTP"`.
- `method` - (Optional) The request method to use. Default is `"POST"`.

_Required_: Yes

_Type_: List of <a href="channeldefinition.md">ChannelDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The inline hook display name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The type of hook to trigger. Currently, the only supported type is `"HTTP"`.
- `method` - (Optional) The request method to use. Default is `"POST"`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

Version of the channel. The currently-supported version is `"1.0.0"`.
- `uri` - (Required) The URI the hook will hit.
- `type` - (Optional) The type of hook to trigger. Currently, the only supported type is `"HTTP"`.
- `method` - (Optional) The request method to use. Default is `"POST"`.

_Required_: Yes

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
