# Terraform::Icinga2::Notification

Configures an Icinga2 notification resource. This allows notifications to be configured, updated,
and deleted.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Icinga2::Notification",
    "Properties" : {
        "<a href="#command" title="Command">Command</a>" : <i>String</i>,
        "<a href="#hostname" title="Hostname">Hostname</a>" : <i>String</i>,
        "<a href="#interval" title="Interval">Interval</a>" : <i>Double</i>,
        "<a href="#servicename" title="Servicename">Servicename</a>" : <i>String</i>,
        "<a href="#templates" title="Templates">Templates</a>" : <i>[ String, ... ]</i>,
        "<a href="#users" title="Users">Users</a>" : <i>[ String, ... ]</i>,
        "<a href="#vars" title="Vars">Vars</a>" : <i>[ <a href="vars.md">Vars</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Icinga2::Notification
Properties:
    <a href="#command" title="Command">Command</a>: <i>String</i>
    <a href="#hostname" title="Hostname">Hostname</a>: <i>String</i>
    <a href="#interval" title="Interval">Interval</a>: <i>Double</i>
    <a href="#servicename" title="Servicename">Servicename</a>: <i>String</i>
    <a href="#templates" title="Templates">Templates</a>: <i>
      - String</i>
    <a href="#users" title="Users">Users</a>: <i>
      - String</i>
    <a href="#vars" title="Vars">Vars</a>: <i>
      - <a href="vars.md">Vars</a></i>
</pre>

## Properties

#### Command

Notification command to use.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hostname

The hostname the notification applies to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interval

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Servicename

Service to send notification for.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Templates

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Users

List of users to notification.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vars

_Required_: No

_Type_: List of <a href="vars.md">Vars</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

