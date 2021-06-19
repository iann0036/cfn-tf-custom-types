# TF::AzureRM::BlueprintAssignment

Manages a Blueprint Assignment resource

~> **NOTE:** Azure Blueprints are in Preview and potentially subject to breaking change without notice.

~> **NOTE:** Azure Blueprint Assignments can only be applied to Subscriptions.  Assignments to Management Groups is not currently supported by the service or by Terraform.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::BlueprintAssignment",
    "Properties" : {
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#lockexcludeprincipals" title="LockExcludePrincipals">LockExcludePrincipals</a>" : <i>[ String, ... ]</i>,
        "<a href="#lockmode" title="LockMode">LockMode</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#parametervalues" title="ParameterValues">ParameterValues</a>" : <i>String</i>,
        "<a href="#resourcegroups" title="ResourceGroups">ResourceGroups</a>" : <i>String</i>,
        "<a href="#targetsubscriptionid" title="TargetSubscriptionId">TargetSubscriptionId</a>" : <i>String</i>,
        "<a href="#versionid" title="VersionId">VersionId</a>" : <i>String</i>,
        "<a href="#identity" title="Identity">Identity</a>" : <i>[ <a href="identitydefinition.md">IdentityDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureRM::BlueprintAssignment
Properties:
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#lockexcludeprincipals" title="LockExcludePrincipals">LockExcludePrincipals</a>: <i>
      - String</i>
    <a href="#lockmode" title="LockMode">LockMode</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#parametervalues" title="ParameterValues">ParameterValues</a>: <i>String</i>
    <a href="#resourcegroups" title="ResourceGroups">ResourceGroups</a>: <i>String</i>
    <a href="#targetsubscriptionid" title="TargetSubscriptionId">TargetSubscriptionId</a>: <i>String</i>
    <a href="#versionid" title="VersionId">VersionId</a>: <i>String</i>
    <a href="#identity" title="Identity">Identity</a>: <i>
      - <a href="identitydefinition.md">IdentityDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Location

The Azure location of the Assignment.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LockExcludePrincipals

a list of up to 5 Principal IDs that are permitted to bypass the locks applied by the Blueprint.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LockMode

The locking mode of the Blueprint Assignment.  One of `None` (Default), `AllResourcesReadOnly`, or `AlResourcesDoNotDelete`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the Blueprint Assignment.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ParameterValues

a JSON string to supply Blueprint Assignment parameter values.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroups

a JSON string to supply the Blueprint Resource Group information.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetSubscriptionId

The Subscription ID the Blueprint Published Version is to be applied to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VersionId

The ID of the Published Version of the blueprint to be assigned.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Identity

_Required_: No

_Type_: List of <a href="identitydefinition.md">IdentityDefinition</a>

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

#### BlueprintName

Returns the <code>BlueprintName</code> value.

#### Description

Returns the <code>Description</code> value.

#### DisplayName

Returns the <code>DisplayName</code> value.

#### Id

Returns the <code>Id</code> value.

#### Type

The Identity type for the Managed Service Identity. Currently only `UserAssigned` is supported.

