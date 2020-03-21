# Terraform::OCI::WaasWaasPolicy WafConfig AddressRateLimiting

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allowedrateperaddress" title="AllowedRatePerAddress">AllowedRatePerAddress</a>" : <i>Double</i>,
    "<a href="#blockresponsecode" title="BlockResponseCode">BlockResponseCode</a>" : <i>Double</i>,
    "<a href="#isenabled" title="IsEnabled">IsEnabled</a>" : <i>Boolean</i>,
    "<a href="#maxdelayedcountperaddress" title="MaxDelayedCountPerAddress">MaxDelayedCountPerAddress</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#allowedrateperaddress" title="AllowedRatePerAddress">AllowedRatePerAddress</a>: <i>Double</i>
<a href="#blockresponsecode" title="BlockResponseCode">BlockResponseCode</a>: <i>Double</i>
<a href="#isenabled" title="IsEnabled">IsEnabled</a>: <i>Boolean</i>
<a href="#maxdelayedcountperaddress" title="MaxDelayedCountPerAddress">MaxDelayedCountPerAddress</a>: <i>Double</i>
</pre>

## Properties

#### AllowedRatePerAddress

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockResponseCode

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsEnabled

_Required_: Yes
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxDelayedCountPerAddress

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

