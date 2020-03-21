# Terraform::PagerDuty::Extension

An [extension](https://v2.developer.pagerduty.com/v2/page/api-reference#!/Extensions/post_extensions) can be associated with a service.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::PagerDuty::Extension",
    "Properties" : {
        "<a href="#config" title="Config">Config</a>" : <i>String</i>,
        "<a href="#endpointurl" title="EndpointUrl">EndpointUrl</a>" : <i>String</i>,
        "<a href="#extensionobjects" title="ExtensionObjects">ExtensionObjects</a>" : <i>[ String, ... ]</i>,
        "<a href="#extensionschema" title="ExtensionSchema">ExtensionSchema</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::PagerDuty::Extension
Properties:
    <a href="#config" title="Config">Config</a>: <i>String</i>
    <a href="#endpointurl" title="EndpointUrl">EndpointUrl</a>: <i>String</i>
    <a href="#extensionobjects" title="ExtensionObjects">ExtensionObjects</a>: <i>
      - String</i>
    <a href="#extensionschema" title="ExtensionSchema">ExtensionSchema</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### Config

The configuration of the service extension as string containing plain JSON-encoded data.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndpointUrl

The url of the extension.
**Note:** The [endpoint URL is Optional API wise](https://api-reference.pagerduty.com/#!/Extensions/post_extensions) in most cases. But in some cases it is a _Required_ parameter. For example, `pagerduty_extension_schema` named `Generic V2 Webhook` doesn't accept `pagerduty_extension` with no `endpoint_url`, but one with named `Slack` accepts.
* `extension_schema` - (Required) This is the schema for this extension.
* `extension_objects` - (Required) This is the objects for which the extension applies (An array of service ids).
* `config` - (Optional) The configuration of the service extension as string containing plain JSON-encoded data.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtensionObjects

This is the objects for which the extension applies (An array of service ids).
* `config` - (Optional) The configuration of the service extension as string containing plain JSON-encoded data.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtensionSchema

This is the schema for this extension.
* `extension_objects` - (Required) This is the objects for which the extension applies (An array of service ids).
* `config` - (Optional) The configuration of the service extension as string containing plain JSON-encoded data.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the service extension.
* `endpoint_url` - (Required|Optional) The url of the extension.
**Note:** The [endpoint URL is Optional API wise](https://api-reference.pagerduty.com/#!/Extensions/post_extensions) in most cases. But in some cases it is a _Required_ parameter. For example, `pagerduty_extension_schema` named `Generic V2 Webhook` doesn't accept `pagerduty_extension` with no `endpoint_url`, but one with named `Slack` accepts.
* `extension_schema` - (Required) This is the schema for this extension.
* `extension_objects` - (Required) This is the objects for which the extension applies (An array of service ids).
* `config` - (Optional) The configuration of the service extension as string containing plain JSON-encoded data.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### HtmlUrl

Returns the <code>HtmlUrl</code> value.

