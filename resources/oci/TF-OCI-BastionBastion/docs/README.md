# TF::OCI::BastionBastion

This resource provides the Bastion resource in Oracle Cloud Infrastructure Bastion service.

Creates a new bastion. A bastion provides secured, public access to target resources in the cloud that you cannot otherwise reach from the internet. A bastion resides in a public subnet and establishes the network infrastructure needed to connect a user to a target resource in a private subnet.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OCI::BastionBastion",
    "Properties" : {
        "<a href="#bastiontype" title="BastionType">BastionType</a>" : <i>String</i>,
        "<a href="#clientcidrblockallowlist" title="ClientCidrBlockAllowList">ClientCidrBlockAllowList</a>" : <i>[ String, ... ]</i>,
        "<a href="#compartmentid" title="CompartmentId">CompartmentId</a>" : <i>String</i>,
        "<a href="#definedtags" title="DefinedTags">DefinedTags</a>" : <i>[ <a href="definedtagsdefinition.md">DefinedTagsDefinition</a>, ... ]</i>,
        "<a href="#freeformtags" title="FreeformTags">FreeformTags</a>" : <i>[ <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a>, ... ]</i>,
        "<a href="#maxsessionttlinseconds" title="MaxSessionTtlInSeconds">MaxSessionTtlInSeconds</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#phonebookentry" title="PhoneBookEntry">PhoneBookEntry</a>" : <i>String</i>,
        "<a href="#staticjumphostipaddresses" title="StaticJumpHostIpAddresses">StaticJumpHostIpAddresses</a>" : <i>[ String, ... ]</i>,
        "<a href="#targetsubnetid" title="TargetSubnetId">TargetSubnetId</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OCI::BastionBastion
Properties:
    <a href="#bastiontype" title="BastionType">BastionType</a>: <i>String</i>
    <a href="#clientcidrblockallowlist" title="ClientCidrBlockAllowList">ClientCidrBlockAllowList</a>: <i>
      - String</i>
    <a href="#compartmentid" title="CompartmentId">CompartmentId</a>: <i>String</i>
    <a href="#definedtags" title="DefinedTags">DefinedTags</a>: <i>
      - <a href="definedtagsdefinition.md">DefinedTagsDefinition</a></i>
    <a href="#freeformtags" title="FreeformTags">FreeformTags</a>: <i>
      - <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a></i>
    <a href="#maxsessionttlinseconds" title="MaxSessionTtlInSeconds">MaxSessionTtlInSeconds</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#phonebookentry" title="PhoneBookEntry">PhoneBookEntry</a>: <i>String</i>
    <a href="#staticjumphostipaddresses" title="StaticJumpHostIpAddresses">StaticJumpHostIpAddresses</a>: <i>
      - String</i>
    <a href="#targetsubnetid" title="TargetSubnetId">TargetSubnetId</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### BastionType

The type of bastion. Use `standard`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientCidrBlockAllowList

(Updatable) A list of address ranges in CIDR notation that you want to allow to connect to sessions hosted by this bastion.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompartmentId

(Updatable) The unique identifier (OCID) of the compartment where the bastion is located.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefinedTags

(Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`.

_Required_: No

_Type_: List of <a href="definedtagsdefinition.md">DefinedTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeformTags

(Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`.

_Required_: No

_Type_: List of <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxSessionTtlInSeconds

(Updatable) The maximum amount of time that any session on the bastion can remain active.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the bastion, which can't be changed after creation.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PhoneBookEntry

The phonebook entry of the customer's team, which can't be changed after creation. Not applicable to `standard` bastions.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaticJumpHostIpAddresses

(Updatable) A list of IP addresses of the hosts that the bastion has access to. Not applicable to `standard` bastions.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetSubnetId

The unique identifier (OCID) of the subnet that the bastion connects to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

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

#### LifecycleDetails

Returns the <code>LifecycleDetails</code> value.

#### MaxSessionsAllowed

Returns the <code>MaxSessionsAllowed</code> value.

#### PrivateEndpointIpAddress

Returns the <code>PrivateEndpointIpAddress</code> value.

#### State

Returns the <code>State</code> value.

#### SystemTags

Returns the <code>SystemTags</code> value.

#### TargetVcnId

Returns the <code>TargetVcnId</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

#### TimeUpdated

Returns the <code>TimeUpdated</code> value.

