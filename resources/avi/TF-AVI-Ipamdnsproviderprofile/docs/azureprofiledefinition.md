# TF::AVI::Ipamdnsproviderprofile AzureProfileDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#egressservicesubnets" title="EgressServiceSubnets">EgressServiceSubnets</a>" : <i>[ String, ... ]</i>,
    "<a href="#resourcegroup" title="ResourceGroup">ResourceGroup</a>" : <i>String</i>,
    "<a href="#subscriptionid" title="SubscriptionId">SubscriptionId</a>" : <i>String</i>,
    "<a href="#usabledomains" title="UsableDomains">UsableDomains</a>" : <i>[ String, ... ]</i>,
    "<a href="#usablenetworkuuids" title="UsableNetworkUuids">UsableNetworkUuids</a>" : <i>[ String, ... ]</i>,
    "<a href="#useenhancedha" title="UseEnhancedHa">UseEnhancedHa</a>" : <i>Boolean</i>,
    "<a href="#usestandardalb" title="UseStandardAlb">UseStandardAlb</a>" : <i>Boolean</i>,
    "<a href="#virtualnetworkids" title="VirtualNetworkIds">VirtualNetworkIds</a>" : <i>[ String, ... ]</i>,
    "<a href="#azureserviceprincipal" title="AzureServiceprincipal">AzureServiceprincipal</a>" : <i>[ <a href="azureserviceprincipaldefinition.md">AzureServiceprincipalDefinition</a>, ... ]</i>,
    "<a href="#azureuserpass" title="AzureUserpass">AzureUserpass</a>" : <i>[ <a href="azureuserpassdefinition.md">AzureUserpassDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#egressservicesubnets" title="EgressServiceSubnets">EgressServiceSubnets</a>: <i>
      - String</i>
<a href="#resourcegroup" title="ResourceGroup">ResourceGroup</a>: <i>String</i>
<a href="#subscriptionid" title="SubscriptionId">SubscriptionId</a>: <i>String</i>
<a href="#usabledomains" title="UsableDomains">UsableDomains</a>: <i>
      - String</i>
<a href="#usablenetworkuuids" title="UsableNetworkUuids">UsableNetworkUuids</a>: <i>
      - String</i>
<a href="#useenhancedha" title="UseEnhancedHa">UseEnhancedHa</a>: <i>Boolean</i>
<a href="#usestandardalb" title="UseStandardAlb">UseStandardAlb</a>: <i>Boolean</i>
<a href="#virtualnetworkids" title="VirtualNetworkIds">VirtualNetworkIds</a>: <i>
      - String</i>
<a href="#azureserviceprincipal" title="AzureServiceprincipal">AzureServiceprincipal</a>: <i>
      - <a href="azureserviceprincipaldefinition.md">AzureServiceprincipalDefinition</a></i>
<a href="#azureuserpass" title="AzureUserpass">AzureUserpass</a>: <i>
      - <a href="azureuserpassdefinition.md">AzureUserpassDefinition</a></i>
</pre>

## Properties

#### EgressServiceSubnets

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroup

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubscriptionId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsableDomains

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsableNetworkUuids

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseEnhancedHa

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseStandardAlb

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualNetworkIds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureServiceprincipal

_Required_: No

_Type_: List of <a href="azureserviceprincipaldefinition.md">AzureServiceprincipalDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureUserpass

_Required_: No

_Type_: List of <a href="azureuserpassdefinition.md">AzureUserpassDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

