# Terraform::Vault::AzureAuthBackendRole

Manages an Azure auth backend role in a Vault server. Roles constrain the
instances or principals that can perform the login operation against the
backend. See the [Vault
documentation](https://www.vaultproject.io/docs/auth/azure.html) for more
information.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Vault::AzureAuthBackendRole",
    "Properties" : {
        "<a href="#backend" title="Backend">Backend</a>" : <i>String</i>,
        "<a href="#boundgroupids" title="BoundGroupIds">BoundGroupIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#boundlocations" title="BoundLocations">BoundLocations</a>" : <i>[ String, ... ]</i>,
        "<a href="#boundresourcegroups" title="BoundResourceGroups">BoundResourceGroups</a>" : <i>[ String, ... ]</i>,
        "<a href="#boundscalesets" title="BoundScaleSets">BoundScaleSets</a>" : <i>[ String, ... ]</i>,
        "<a href="#boundserviceprincipalids" title="BoundServicePrincipalIds">BoundServicePrincipalIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#boundsubscriptionids" title="BoundSubscriptionIds">BoundSubscriptionIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#maxttl" title="MaxTtl">MaxTtl</a>" : <i>Double</i>,
        "<a href="#period" title="Period">Period</a>" : <i>Double</i>,
        "<a href="#policies" title="Policies">Policies</a>" : <i>[ String, ... ]</i>,
        "<a href="#role" title="Role">Role</a>" : <i>String</i>,
        "<a href="#tokenboundcidrs" title="TokenBoundCidrs">TokenBoundCidrs</a>" : <i>[ String, ... ]</i>,
        "<a href="#tokenexplicitmaxttl" title="TokenExplicitMaxTtl">TokenExplicitMaxTtl</a>" : <i>Double</i>,
        "<a href="#tokenmaxttl" title="TokenMaxTtl">TokenMaxTtl</a>" : <i>Double</i>,
        "<a href="#tokennodefaultpolicy" title="TokenNoDefaultPolicy">TokenNoDefaultPolicy</a>" : <i>Boolean</i>,
        "<a href="#tokennumuses" title="TokenNumUses">TokenNumUses</a>" : <i>Double</i>,
        "<a href="#tokenperiod" title="TokenPeriod">TokenPeriod</a>" : <i>Double</i>,
        "<a href="#tokenpolicies" title="TokenPolicies">TokenPolicies</a>" : <i>[ String, ... ]</i>,
        "<a href="#tokenttl" title="TokenTtl">TokenTtl</a>" : <i>Double</i>,
        "<a href="#tokentype" title="TokenType">TokenType</a>" : <i>String</i>,
        "<a href="#ttl" title="Ttl">Ttl</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Vault::AzureAuthBackendRole
Properties:
    <a href="#backend" title="Backend">Backend</a>: <i>String</i>
    <a href="#boundgroupids" title="BoundGroupIds">BoundGroupIds</a>: <i>
      - String</i>
    <a href="#boundlocations" title="BoundLocations">BoundLocations</a>: <i>
      - String</i>
    <a href="#boundresourcegroups" title="BoundResourceGroups">BoundResourceGroups</a>: <i>
      - String</i>
    <a href="#boundscalesets" title="BoundScaleSets">BoundScaleSets</a>: <i>
      - String</i>
    <a href="#boundserviceprincipalids" title="BoundServicePrincipalIds">BoundServicePrincipalIds</a>: <i>
      - String</i>
    <a href="#boundsubscriptionids" title="BoundSubscriptionIds">BoundSubscriptionIds</a>: <i>
      - String</i>
    <a href="#maxttl" title="MaxTtl">MaxTtl</a>: <i>Double</i>
    <a href="#period" title="Period">Period</a>: <i>Double</i>
    <a href="#policies" title="Policies">Policies</a>: <i>
      - String</i>
    <a href="#role" title="Role">Role</a>: <i>String</i>
    <a href="#tokenboundcidrs" title="TokenBoundCidrs">TokenBoundCidrs</a>: <i>
      - String</i>
    <a href="#tokenexplicitmaxttl" title="TokenExplicitMaxTtl">TokenExplicitMaxTtl</a>: <i>Double</i>
    <a href="#tokenmaxttl" title="TokenMaxTtl">TokenMaxTtl</a>: <i>Double</i>
    <a href="#tokennodefaultpolicy" title="TokenNoDefaultPolicy">TokenNoDefaultPolicy</a>: <i>Boolean</i>
    <a href="#tokennumuses" title="TokenNumUses">TokenNumUses</a>: <i>Double</i>
    <a href="#tokenperiod" title="TokenPeriod">TokenPeriod</a>: <i>Double</i>
    <a href="#tokenpolicies" title="TokenPolicies">TokenPolicies</a>: <i>
      - String</i>
    <a href="#tokenttl" title="TokenTtl">TokenTtl</a>: <i>Double</i>
    <a href="#tokentype" title="TokenType">TokenType</a>: <i>String</i>
    <a href="#ttl" title="Ttl">Ttl</a>: <i>Double</i>
</pre>

## Properties

#### Backend

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BoundGroupIds

If set, defines a constraint on the groups
that can perform the login operation that they should be using the group
ID specified by this field.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BoundLocations

If set, defines a constraint on the virtual machines
that can perform the login operation that the location in their identity
document must match the one specified by this field.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BoundResourceGroups

If set, defines a constraint on the virtual
machiness that can perform the login operation that they be associated with
the resource group that matches the value specified by this field.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BoundScaleSets

If set, defines a constraint on the virtual
machines that can perform the login operation that they must match the scale set
specified by this field.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BoundServicePrincipalIds

If set, defines a constraint on the
service principals that can perform the login operation that they should be possess
the ids specified by this field.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BoundSubscriptionIds

If set, defines a constraint on the subscriptions
that can perform the login operation to ones which  matches the value specified by this
field.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxTtl

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Period

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Policies

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Role

The name of the role.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenBoundCidrs

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenExplicitMaxTtl

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenMaxTtl

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenNoDefaultPolicy

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenNumUses

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenPeriod

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenPolicies

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenTtl

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ttl

_Required_: No

_Type_: Double

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

