# TF::AzureDevOps::ServiceendpointRunpipeline

Manages a Azure DevOps Service Connection service endpoint within Azure DevOps. Allows to run downstream pipelines, monitoring their execution, collecting and consolidating artefacts produced in the delegate pipelines (yaml block `task: RunPipelines@1`). More details on Marketplace page: [RunPipelines](https://marketplace.visualstudio.com/items?itemName=CSE-DevOps.RunPipelines)

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureDevOps::ServiceendpointRunpipeline",
    "Properties" : {
        "<a href="#authorization" title="Authorization">Authorization</a>" : <i>[ <a href="authorizationdefinition.md">AuthorizationDefinition</a>, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#organizationname" title="OrganizationName">OrganizationName</a>" : <i>String</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>,
        "<a href="#serviceendpointname" title="ServiceEndpointName">ServiceEndpointName</a>" : <i>String</i>,
        "<a href="#authpersonal" title="AuthPersonal">AuthPersonal</a>" : <i>[ <a href="authpersonaldefinition.md">AuthPersonalDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureDevOps::ServiceendpointRunpipeline
Properties:
    <a href="#authorization" title="Authorization">Authorization</a>: <i>
      - <a href="authorizationdefinition.md">AuthorizationDefinition</a></i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#organizationname" title="OrganizationName">OrganizationName</a>: <i>String</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
    <a href="#serviceendpointname" title="ServiceEndpointName">ServiceEndpointName</a>: <i>String</i>
    <a href="#authpersonal" title="AuthPersonal">AuthPersonal</a>: <i>
      - <a href="authpersonaldefinition.md">AuthPersonalDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Authorization

_Required_: No

_Type_: List of <a href="authorizationdefinition.md">AuthorizationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The Service Endpoint description. Defaults to `Managed by Terraform`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OrganizationName

The organization name used for `Organization Url` and `Release API Url` fields.
- `auth_personal` - (Required) An `auth_personal` block as documented below. Allows connecting using a personal access token.
- `description` - (Optional) The Service Endpoint description. Defaults to `Managed by Terraform`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

The project ID or project name.
- `service_endpoint_name` - (Required) The Service Endpoint name.
- `organization_name` - (Required) The organization name used for `Organization Url` and `Release API Url` fields.
- `auth_personal` - (Required) An `auth_personal` block as documented below. Allows connecting using a personal access token.
- `description` - (Optional) The Service Endpoint description. Defaults to `Managed by Terraform`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceEndpointName

The Service Endpoint name.
- `organization_name` - (Required) The organization name used for `Organization Url` and `Release API Url` fields.
- `auth_personal` - (Required) An `auth_personal` block as documented below. Allows connecting using a personal access token.
- `description` - (Optional) The Service Endpoint description. Defaults to `Managed by Terraform`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthPersonal

_Required_: No

_Type_: List of <a href="authpersonaldefinition.md">AuthPersonalDefinition</a>

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
