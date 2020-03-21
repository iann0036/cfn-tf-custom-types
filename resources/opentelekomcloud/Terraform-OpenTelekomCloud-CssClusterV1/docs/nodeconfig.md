# Terraform::OpenTelekomCloud::CssClusterV1 NodeConfig

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>" : <i>String</i>,
    "<a href="#flavor" title="Flavor">Flavor</a>" : <i>String</i>,
    "<a href="#networkinfo" title="NetworkInfo">NetworkInfo</a>" : <i>[ <a href="nodeconfig-networkinfo.md">NetworkInfo</a>, ... ]</i>,
    "<a href="#volume" title="Volume">Volume</a>" : <i>[ <a href="nodeconfig-volume.md">Volume</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>: <i>String</i>
<a href="#flavor" title="Flavor">Flavor</a>: <i>String</i>
<a href="#networkinfo" title="NetworkInfo">NetworkInfo</a>: <i>
      - <a href="nodeconfig-networkinfo.md">NetworkInfo</a></i>
<a href="#volume" title="Volume">Volume</a>: <i>
      - <a href="nodeconfig-volume.md">Volume</a></i>
</pre>

## Properties

#### AvailabilityZone

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Flavor

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkInfo

_Required_: No
_Type_: List of <a href="nodeconfig-networkinfo.md">NetworkInfo</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Volume

_Required_: No
_Type_: List of <a href="nodeconfig-volume.md">Volume</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

