# TF::GoogleBeta::GoogleIamWorkloadIdentityPoolProvider

CloudFormation equivalent of google_iam_workload_identity_pool_provider

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::GoogleBeta::GoogleIamWorkloadIdentityPoolProvider",
    "Properties" : {
        "<a href="#attributecondition" title="AttributeCondition">AttributeCondition</a>" : <i>String</i>,
        "<a href="#attributemapping" title="AttributeMapping">AttributeMapping</a>" : <i>[ <a href="attributemappingdefinition.md">AttributeMappingDefinition</a>, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#disabled" title="Disabled">Disabled</a>" : <i>Boolean</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#workloadidentitypoolid" title="WorkloadIdentityPoolId">WorkloadIdentityPoolId</a>" : <i>String</i>,
        "<a href="#workloadidentitypoolproviderid" title="WorkloadIdentityPoolProviderId">WorkloadIdentityPoolProviderId</a>" : <i>String</i>,
        "<a href="#aws" title="Aws">Aws</a>" : <i>[ <a href="awsdefinition.md">AwsDefinition</a>, ... ]</i>,
        "<a href="#oidc" title="Oidc">Oidc</a>" : <i>[ <a href="oidcdefinition.md">OidcDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::GoogleBeta::GoogleIamWorkloadIdentityPoolProvider
Properties:
    <a href="#attributecondition" title="AttributeCondition">AttributeCondition</a>: <i>String</i>
    <a href="#attributemapping" title="AttributeMapping">AttributeMapping</a>: <i>
      - <a href="attributemappingdefinition.md">AttributeMappingDefinition</a></i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#disabled" title="Disabled">Disabled</a>: <i>Boolean</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#workloadidentitypoolid" title="WorkloadIdentityPoolId">WorkloadIdentityPoolId</a>: <i>String</i>
    <a href="#workloadidentitypoolproviderid" title="WorkloadIdentityPoolProviderId">WorkloadIdentityPoolProviderId</a>: <i>String</i>
    <a href="#aws" title="Aws">Aws</a>: <i>
      - <a href="awsdefinition.md">AwsDefinition</a></i>
    <a href="#oidc" title="Oidc">Oidc</a>: <i>
      - <a href="oidcdefinition.md">OidcDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AttributeCondition

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AttributeMapping

_Required_: No

_Type_: List of <a href="attributemappingdefinition.md">AttributeMappingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkloadIdentityPoolId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkloadIdentityPoolProviderId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Aws

_Required_: No

_Type_: List of <a href="awsdefinition.md">AwsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Oidc

_Required_: No

_Type_: List of <a href="oidcdefinition.md">OidcDefinition</a>

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

#### Name

Returns the <code>Name</code> value.

#### State

Returns the <code>State</code> value.

