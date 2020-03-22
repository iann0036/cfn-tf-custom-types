# Terraform::Skytap::Environment

Provides a Skytap Environment resource. An environment consists of one or more virtual machines, networks, 
and associated settings and metadata. Unlike a template, an environment can be run and have most of its settings 
modified. When an environment is created all of its VMs will be run.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Skytap::Environment",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#outboundtraffic" title="OutboundTraffic">OutboundTraffic</a>" : <i>Boolean</i>,
        "<a href="#routable" title="Routable">Routable</a>" : <i>Boolean</i>,
        "<a href="#shutdownattime" title="ShutdownAtTime">ShutdownAtTime</a>" : <i>String</i>,
        "<a href="#shutdownonidle" title="ShutdownOnIdle">ShutdownOnIdle</a>" : <i>Double</i>,
        "<a href="#suspendattime" title="SuspendAtTime">SuspendAtTime</a>" : <i>String</i>,
        "<a href="#suspendonidle" title="SuspendOnIdle">SuspendOnIdle</a>" : <i>Double</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#templateid" title="TemplateId">TemplateId</a>" : <i>String</i>,
        "<a href="#userdata" title="UserData">UserData</a>" : <i>String</i>,
        "<a href="#label" title="Label">Label</a>" : <i>[ <a href="label.md">Label</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Skytap::Environment
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#outboundtraffic" title="OutboundTraffic">OutboundTraffic</a>: <i>Boolean</i>
    <a href="#routable" title="Routable">Routable</a>: <i>Boolean</i>
    <a href="#shutdownattime" title="ShutdownAtTime">ShutdownAtTime</a>: <i>String</i>
    <a href="#shutdownonidle" title="ShutdownOnIdle">ShutdownOnIdle</a>: <i>Double</i>
    <a href="#suspendattime" title="SuspendAtTime">SuspendAtTime</a>: <i>String</i>
    <a href="#suspendonidle" title="SuspendOnIdle">SuspendOnIdle</a>: <i>Double</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#templateid" title="TemplateId">TemplateId</a>: <i>String</i>
    <a href="#userdata" title="UserData">UserData</a>: <i>String</i>
    <a href="#label" title="Label">Label</a>: <i>
      - <a href="label.md">Label</a></i>
</pre>

## Properties

#### Description

User-defined description of the environment. Limited to 1000 characters. Null allowed. UTF-8 character type.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

User-defined name of the environment. Limited to 255 characters. UTF-8 character type. Will default to source template’s name if null is provided.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutboundTraffic

Indicates whether networks in the environment can send outbound traffic.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Routable

Indicates whether networks within the environment can route traffic to one another.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShutdownAtTime

The date and time that the environment will be automatically shut down. Format: yyyy/mm/dd hh:mm:ss. By default, the suspend time uses the UTC offset for the time zone defined in your user account settings. Optionally, a different UTC offset can be supplied (for example: 2018/07/20 14:20:00 -0000). The value in the API response is converted to your time zone.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShutdownOnIdle

The number of seconds an environment can be idle before it is automatically shut down. Valid range: 300 to 86400 seconds (5 minutes to 1 day).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SuspendAtTime

The date and time that the environment will be automatically suspended. Format: yyyy/mm/dd hh:mm:ss. By default, the suspend time uses the UTC offset for the time zone defined in your user account settings. Optionally, a different UTC offset can be supplied (for example: 2018/07/20 14:20:00 -0000). The value in the API response is converted to your time zone.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SuspendOnIdle

The number of seconds an environment can be idle before it is automatically suspended. Valid range: 300 to 86400 seconds (5 minutes to 1 day).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

List of environment tags.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateId

ID of the template you want to create an environment from. If updating with a new one then the environment will be recreated.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserData

Environment user data, available from the metadata server and the skytap api.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Label

_Required_: No

_Type_: List of <a href="label.md">Label</a>

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

