# TF::GoogleBeta::GoogleOsConfigGuestPolicies

CloudFormation equivalent of google_os_config_guest_policies

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::GoogleBeta::GoogleOsConfigGuestPolicies",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#etag" title="Etag">Etag</a>" : <i>String</i>,
        "<a href="#guestpolicyid" title="GuestPolicyId">GuestPolicyId</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#assignment" title="Assignment">Assignment</a>" : <i>[ <a href="assignmentdefinition.md">AssignmentDefinition</a>, ... ]</i>,
        "<a href="#packagerepositories" title="PackageRepositories">PackageRepositories</a>" : <i>[ <a href="packagerepositoriesdefinition.md">PackageRepositoriesDefinition</a>, ... ]</i>,
        "<a href="#packages" title="Packages">Packages</a>" : <i>[ <a href="packagesdefinition.md">PackagesDefinition</a>, ... ]</i>,
        "<a href="#recipes" title="Recipes">Recipes</a>" : <i>[ <a href="recipesdefinition.md">RecipesDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::GoogleBeta::GoogleOsConfigGuestPolicies
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#etag" title="Etag">Etag</a>: <i>String</i>
    <a href="#guestpolicyid" title="GuestPolicyId">GuestPolicyId</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#assignment" title="Assignment">Assignment</a>: <i>
      - <a href="assignmentdefinition.md">AssignmentDefinition</a></i>
    <a href="#packagerepositories" title="PackageRepositories">PackageRepositories</a>: <i>
      - <a href="packagerepositoriesdefinition.md">PackageRepositoriesDefinition</a></i>
    <a href="#packages" title="Packages">Packages</a>: <i>
      - <a href="packagesdefinition.md">PackagesDefinition</a></i>
    <a href="#recipes" title="Recipes">Recipes</a>: <i>
      - <a href="recipesdefinition.md">RecipesDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Etag

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuestPolicyId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Assignment

_Required_: No

_Type_: List of <a href="assignmentdefinition.md">AssignmentDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PackageRepositories

_Required_: No

_Type_: List of <a href="packagerepositoriesdefinition.md">PackageRepositoriesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Packages

_Required_: No

_Type_: List of <a href="packagesdefinition.md">PackagesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Recipes

_Required_: No

_Type_: List of <a href="recipesdefinition.md">RecipesDefinition</a>

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

#### CreateTime

Returns the <code>CreateTime</code> value.

#### Id

Returns the <code>Id</code> value.

#### Name

Returns the <code>Name</code> value.

#### UpdateTime

Returns the <code>UpdateTime</code> value.

