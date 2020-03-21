# Terraform::Panos::PanoramaEdl

This resource allows you to add/update/delete Panorama external dynamic lists (EDL).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Panos::PanoramaEdl",
    "Properties" : {
        "<a href="#certificateprofile" title="CertificateProfile">CertificateProfile</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#devicegroup" title="DeviceGroup">DeviceGroup</a>" : <i>String</i>,
        "<a href="#exceptions" title="Exceptions">Exceptions</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#repeat" title="Repeat">Repeat</a>" : <i>String</i>,
        "<a href="#repeatat" title="RepeatAt">RepeatAt</a>" : <i>String</i>,
        "<a href="#repeatdayofmonth" title="RepeatDayOfMonth">RepeatDayOfMonth</a>" : <i>Double</i>,
        "<a href="#repeatdayofweek" title="RepeatDayOfWeek">RepeatDayOfWeek</a>" : <i>String</i>,
        "<a href="#source" title="Source">Source</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#username" title="Username">Username</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Panos::PanoramaEdl
Properties:
    <a href="#certificateprofile" title="CertificateProfile">CertificateProfile</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#devicegroup" title="DeviceGroup">DeviceGroup</a>: <i>String</i>
    <a href="#exceptions" title="Exceptions">Exceptions</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#repeat" title="Repeat">Repeat</a>: <i>String</i>
    <a href="#repeatat" title="RepeatAt">RepeatAt</a>: <i>String</i>
    <a href="#repeatdayofmonth" title="RepeatDayOfMonth">RepeatDayOfMonth</a>: <i>Double</i>
    <a href="#repeatdayofweek" title="RepeatDayOfWeek">RepeatDayOfWeek</a>: <i>String</i>
    <a href="#source" title="Source">Source</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#username" title="Username">Username</a>: <i>String</i>
</pre>

## Properties

#### CertificateProfile

Profile for authenticating client certificates.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The object's description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceGroup

The device group (default: `shared`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Exceptions

Provide a list of exception entries.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The object's name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

EDL password.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Repeat

How often to retrieve the EDL.  This can be `hourly` (the
default), `daily`, `weekly`, `monthly`, or `every five minutes` (valid for
PAN-OS 7.1+).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RepeatAt

The time at which to retrieve the EDL.  Please refer
to the section above for how to set this value properly.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RepeatDayOfMonth

If `repeat` is `monthly`, then this should
be set to the desired day of the month.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RepeatDayOfWeek

If `repeat` is `weekly`, then this should
be set to the desired day of the week.  Valid values are `sunday`,
`monday`, `tuesday`, `wednesday`, `thursday`, `friday`, `saturday`, and
`sunday`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

The EDL source URL.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The type of EDL.  This can be `ip` (the default; and the
only valid value for PAN-OS 6.1 - 7.0), `domain`, `url`, or `predefined`
(PAN-OS 8.0+).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Username

EDL username.

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

#### PasswordEnc

Returns the <code>PasswordEnc</code> value.

