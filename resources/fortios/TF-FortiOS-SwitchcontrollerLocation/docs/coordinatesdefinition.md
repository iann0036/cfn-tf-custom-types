# TF::FortiOS::SwitchcontrollerLocation CoordinatesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#altitude" title="Altitude">Altitude</a>" : <i>String</i>,
    "<a href="#altitudeunit" title="AltitudeUnit">AltitudeUnit</a>" : <i>String</i>,
    "<a href="#datum" title="Datum">Datum</a>" : <i>String</i>,
    "<a href="#latitude" title="Latitude">Latitude</a>" : <i>String</i>,
    "<a href="#longitude" title="Longitude">Longitude</a>" : <i>String</i>,
    "<a href="#parentkey" title="ParentKey">ParentKey</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#altitude" title="Altitude">Altitude</a>: <i>String</i>
<a href="#altitudeunit" title="AltitudeUnit">AltitudeUnit</a>: <i>String</i>
<a href="#datum" title="Datum">Datum</a>: <i>String</i>
<a href="#latitude" title="Latitude">Latitude</a>: <i>String</i>
<a href="#longitude" title="Longitude">Longitude</a>: <i>String</i>
<a href="#parentkey" title="ParentKey">ParentKey</a>: <i>String</i>
</pre>

## Properties

#### Altitude

+/- Floating point no. eg. 117.47.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AltitudeUnit

m ( meters), f ( floors). Valid values: `m`, `f`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Datum

WGS84, NAD83, NAD83/MLLW. Valid values: `WGS84`, `NAD83`, `NAD83/MLLW`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Latitude

Floating point start with ( +/- )  or end with ( N or S ) eg. +/-16.67 or 16.67N.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Longitude

Floating point start with ( +/- )  or end with ( E or W ) eg. +/-26.789 or 26.789E.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ParentKey

Parent key name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

