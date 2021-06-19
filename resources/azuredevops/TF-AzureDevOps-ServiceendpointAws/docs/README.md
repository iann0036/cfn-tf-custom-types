# TF::AzureDevOps::ServiceendpointAws

Manages a AWS service endpoint within Azure DevOps. Using this service endpoint requires you to first install [AWS Toolkit for Azure DevOps](https://marketplace.visualstudio.com/items?itemName=AmazonWebServices.aws-vsts-tools).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureDevOps::ServiceendpointAws",
    "Properties" : {
        "<a href="#accesskeyid" title="AccessKeyId">AccessKeyId</a>" : <i>String</i>,
        "<a href="#authorization" title="Authorization">Authorization</a>" : <i>[ <a href="authorizationdefinition.md">AuthorizationDefinition</a>, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#externalid" title="ExternalId">ExternalId</a>" : <i>String</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>,
        "<a href="#rolesessionname" title="RoleSessionName">RoleSessionName</a>" : <i>String</i>,
        "<a href="#roletoassume" title="RoleToAssume">RoleToAssume</a>" : <i>String</i>,
        "<a href="#secretaccesskey" title="SecretAccessKey">SecretAccessKey</a>" : <i>String</i>,
        "<a href="#serviceendpointname" title="ServiceEndpointName">ServiceEndpointName</a>" : <i>String</i>,
        "<a href="#sessiontoken" title="SessionToken">SessionToken</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureDevOps::ServiceendpointAws
Properties:
    <a href="#accesskeyid" title="AccessKeyId">AccessKeyId</a>: <i>String</i>
    <a href="#authorization" title="Authorization">Authorization</a>: <i>
      - <a href="authorizationdefinition.md">AuthorizationDefinition</a></i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#externalid" title="ExternalId">ExternalId</a>: <i>String</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
    <a href="#rolesessionname" title="RoleSessionName">RoleSessionName</a>: <i>String</i>
    <a href="#roletoassume" title="RoleToAssume">RoleToAssume</a>: <i>String</i>
    <a href="#secretaccesskey" title="SecretAccessKey">SecretAccessKey</a>: <i>String</i>
    <a href="#serviceendpointname" title="ServiceEndpointName">ServiceEndpointName</a>: <i>String</i>
    <a href="#sessiontoken" title="SessionToken">SessionToken</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AccessKeyId

The AWS access key ID for signing programmatic requests.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Authorization

_Required_: No

_Type_: List of <a href="authorizationdefinition.md">AuthorizationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The Service Endpoint description. Defaults to `Managed by Terraform`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalId

A unique identifier that is used by third parties when assuming roles in their customers' accounts, aka cross-account role access.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

The project ID or project name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleSessionName

Optional identifier for the assumed role session.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleToAssume

The Amazon Resource Name (ARN) of the role to assume.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretAccessKey

The AWS secret access key for signing programmatic requests.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceEndpointName

The Service Endpoint name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionToken

The AWS session token for signing programmatic requests.

_Required_: No

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

#### SecretAccessKeyHash

Returns the <code>SecretAccessKeyHash</code> value.

#### SessionTokenHash

Returns the <code>SessionTokenHash</code> value.

