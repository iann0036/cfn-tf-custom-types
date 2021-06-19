# TF::FortiOS::SystemAccprofile SysgrpPermissionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#admin" title="Admin">Admin</a>" : <i>String</i>,
    "<a href="#cfg" title="Cfg">Cfg</a>" : <i>String</i>,
    "<a href="#mnt" title="Mnt">Mnt</a>" : <i>String</i>,
    "<a href="#upd" title="Upd">Upd</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#admin" title="Admin">Admin</a>: <i>String</i>
<a href="#cfg" title="Cfg">Cfg</a>: <i>String</i>
<a href="#mnt" title="Mnt">Mnt</a>: <i>String</i>
<a href="#upd" title="Upd">Upd</a>: <i>String</i>
</pre>

## Properties

#### Admin

Administrator Users. Valid values: `none`, `read`, `read-write`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cfg

System Configuration. Valid values: `none`, `read`, `read-write`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mnt

Maintenance. Valid values: `none`, `read`, `read-write`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Upd

FortiGuard Updates. Valid values: `none`, `read`, `read-write`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

