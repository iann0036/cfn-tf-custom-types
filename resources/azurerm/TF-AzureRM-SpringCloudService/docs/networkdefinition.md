# TF::AzureRM::SpringCloudService NetworkDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#appnetworkresourcegroup" title="AppNetworkResourceGroup">AppNetworkResourceGroup</a>" : <i>String</i>,
    "<a href="#appsubnetid" title="AppSubnetId">AppSubnetId</a>" : <i>String</i>,
    "<a href="#cidrranges" title="CidrRanges">CidrRanges</a>" : <i>[ String, ... ]</i>,
    "<a href="#serviceruntimenetworkresourcegroup" title="ServiceRuntimeNetworkResourceGroup">ServiceRuntimeNetworkResourceGroup</a>" : <i>String</i>,
    "<a href="#serviceruntimesubnetid" title="ServiceRuntimeSubnetId">ServiceRuntimeSubnetId</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#appnetworkresourcegroup" title="AppNetworkResourceGroup">AppNetworkResourceGroup</a>: <i>String</i>
<a href="#appsubnetid" title="AppSubnetId">AppSubnetId</a>: <i>String</i>
<a href="#cidrranges" title="CidrRanges">CidrRanges</a>: <i>
      - String</i>
<a href="#serviceruntimenetworkresourcegroup" title="ServiceRuntimeNetworkResourceGroup">ServiceRuntimeNetworkResourceGroup</a>: <i>String</i>
<a href="#serviceruntimesubnetid" title="ServiceRuntimeSubnetId">ServiceRuntimeSubnetId</a>: <i>String</i>
</pre>

## Properties

#### AppNetworkResourceGroup

Specifies the Name of the resource group containing network resources of Azure Spring Cloud Apps. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppSubnetId

Specifies the ID of the Subnet which should host the Spring Boot Applications deployed in this Spring Cloud Service. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CidrRanges

A list of (at least 3) CIDR ranges (at least /16) which are used to host the Spring Cloud infrastructure, which must not overlap with any existing CIDR ranges in the Subnet. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceRuntimeNetworkResourceGroup

Specifies the Name of the resource group containing network resources of Azure Spring Cloud Service Runtime. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceRuntimeSubnetId

Specifies the ID of the Subnet where the Service Runtime components of the Spring Cloud Service will exist. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

