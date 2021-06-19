# TF::Google::AccessContextManagerAccessLevelCondition

Allows configuring a single access level condition to be appended to an access level's conditions.
This resource is intended to be used in cases where it is not possible to compile a full list
of conditions to include in a `google_access_context_manager_access_level` resource,
to enable them to be added separately.

~> **Note:** If this resource is used alongside a `google_access_context_manager_access_level` resource,
the access level resource must have a `lifecycle` block with `ignore_changes = [basic[0].conditions]` so
they don't fight over which service accounts should be included.


To get more information about AccessLevelCondition, see:

* [API documentation](https://cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels)
* How-to Guides
    * [Access Policy Quickstart](https://cloud.google.com/access-context-manager/docs/quickstart)

~> **Warning:** If you are using User ADCs (Application Default Credentials) with this resource,
you must specify a `billing_proje...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Google::AccessContextManagerAccessLevelCondition",
    "Properties" : {
        "<a href="#accesslevel" title="AccessLevel">AccessLevel</a>" : <i>String</i>,
        "<a href="#ipsubnetworks" title="IpSubnetworks">IpSubnetworks</a>" : <i>[ String, ... ]</i>,
        "<a href="#members" title="Members">Members</a>" : <i>[ String, ... ]</i>,
        "<a href="#negate" title="Negate">Negate</a>" : <i>Boolean</i>,
        "<a href="#regions" title="Regions">Regions</a>" : <i>[ String, ... ]</i>,
        "<a href="#requiredaccesslevels" title="RequiredAccessLevels">RequiredAccessLevels</a>" : <i>[ String, ... ]</i>,
        "<a href="#devicepolicy" title="DevicePolicy">DevicePolicy</a>" : <i>[ <a href="devicepolicydefinition.md">DevicePolicyDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Google::AccessContextManagerAccessLevelCondition
Properties:
    <a href="#accesslevel" title="AccessLevel">AccessLevel</a>: <i>String</i>
    <a href="#ipsubnetworks" title="IpSubnetworks">IpSubnetworks</a>: <i>
      - String</i>
    <a href="#members" title="Members">Members</a>: <i>
      - String</i>
    <a href="#negate" title="Negate">Negate</a>: <i>Boolean</i>
    <a href="#regions" title="Regions">Regions</a>: <i>
      - String</i>
    <a href="#requiredaccesslevels" title="RequiredAccessLevels">RequiredAccessLevels</a>: <i>
      - String</i>
    <a href="#devicepolicy" title="DevicePolicy">DevicePolicy</a>: <i>
      - <a href="devicepolicydefinition.md">DevicePolicyDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AccessLevel

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpSubnetworks

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Members

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Negate

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Regions

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequiredAccessLevels

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DevicePolicy

_Required_: No

_Type_: List of <a href="devicepolicydefinition.md">DevicePolicyDefinition</a>

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

