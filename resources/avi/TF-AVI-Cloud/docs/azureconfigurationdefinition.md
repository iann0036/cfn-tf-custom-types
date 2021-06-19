# TF::AVI::Cloud AzureConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#availabilityzones" title="AvailabilityZones">AvailabilityZones</a>" : <i>[ String, ... ]</i>,
    "<a href="#cloudcredentialsref" title="CloudCredentialsRef">CloudCredentialsRef</a>" : <i>String</i>,
    "<a href="#desid" title="DesId">DesId</a>" : <i>String</i>,
    "<a href="#location" title="Location">Location</a>" : <i>String</i>,
    "<a href="#resourcegroup" title="ResourceGroup">ResourceGroup</a>" : <i>String</i>,
    "<a href="#subscriptionid" title="SubscriptionId">SubscriptionId</a>" : <i>String</i>,
    "<a href="#useazuredns" title="UseAzureDns">UseAzureDns</a>" : <i>Boolean</i>,
    "<a href="#useenhancedha" title="UseEnhancedHa">UseEnhancedHa</a>" : <i>Boolean</i>,
    "<a href="#usemanageddisks" title="UseManagedDisks">UseManagedDisks</a>" : <i>Boolean</i>,
    "<a href="#usestandardalb" title="UseStandardAlb">UseStandardAlb</a>" : <i>Boolean</i>,
    "<a href="#networkinfo" title="NetworkInfo">NetworkInfo</a>" : <i>[ <a href="networkinfodefinition.md">NetworkInfoDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#availabilityzones" title="AvailabilityZones">AvailabilityZones</a>: <i>
      - String</i>
<a href="#cloudcredentialsref" title="CloudCredentialsRef">CloudCredentialsRef</a>: <i>String</i>
<a href="#desid" title="DesId">DesId</a>: <i>String</i>
<a href="#location" title="Location">Location</a>: <i>String</i>
<a href="#resourcegroup" title="ResourceGroup">ResourceGroup</a>: <i>String</i>
<a href="#subscriptionid" title="SubscriptionId">SubscriptionId</a>: <i>String</i>
<a href="#useazuredns" title="UseAzureDns">UseAzureDns</a>: <i>Boolean</i>
<a href="#useenhancedha" title="UseEnhancedHa">UseEnhancedHa</a>: <i>Boolean</i>
<a href="#usemanageddisks" title="UseManagedDisks">UseManagedDisks</a>: <i>Boolean</i>
<a href="#usestandardalb" title="UseStandardAlb">UseStandardAlb</a>: <i>Boolean</i>
<a href="#networkinfo" title="NetworkInfo">NetworkInfo</a>: <i>
      - <a href="networkinfodefinition.md">NetworkInfoDefinition</a></i>
</pre>

## Properties

#### AvailabilityZones

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudCredentialsRef

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DesId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroup

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubscriptionId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseAzureDns

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseEnhancedHa

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseManagedDisks

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseStandardAlb

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkInfo

_Required_: No

_Type_: List of <a href="networkinfodefinition.md">NetworkInfoDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

