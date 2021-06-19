# TF::AzureDevOps::ServiceendpointDockerregistry

Manages a Docker Registry service endpoint within Azure DevOps.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureDevOps::ServiceendpointDockerregistry",
    "Properties" : {
        "<a href="#authorization" title="Authorization">Authorization</a>" : <i>[ <a href="authorizationdefinition.md">AuthorizationDefinition</a>, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#dockeremail" title="DockerEmail">DockerEmail</a>" : <i>String</i>,
        "<a href="#dockerpassword" title="DockerPassword">DockerPassword</a>" : <i>String</i>,
        "<a href="#dockerregistry" title="DockerRegistry">DockerRegistry</a>" : <i>String</i>,
        "<a href="#dockerusername" title="DockerUsername">DockerUsername</a>" : <i>String</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>,
        "<a href="#registrytype" title="RegistryType">RegistryType</a>" : <i>String</i>,
        "<a href="#serviceendpointname" title="ServiceEndpointName">ServiceEndpointName</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureDevOps::ServiceendpointDockerregistry
Properties:
    <a href="#authorization" title="Authorization">Authorization</a>: <i>
      - <a href="authorizationdefinition.md">AuthorizationDefinition</a></i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#dockeremail" title="DockerEmail">DockerEmail</a>: <i>String</i>
    <a href="#dockerpassword" title="DockerPassword">DockerPassword</a>: <i>String</i>
    <a href="#dockerregistry" title="DockerRegistry">DockerRegistry</a>: <i>String</i>
    <a href="#dockerusername" title="DockerUsername">DockerUsername</a>: <i>String</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
    <a href="#registrytype" title="RegistryType">RegistryType</a>: <i>String</i>
    <a href="#serviceendpointname" title="ServiceEndpointName">ServiceEndpointName</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Authorization

_Required_: No

_Type_: List of <a href="authorizationdefinition.md">AuthorizationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The name you will use to refer to this service connection in task inputs.
- `docker_registry` - (Optional) The URL of the Docker registry. (Default: "https://index.docker.io/v1/")
- `docker_username` - (Optional) The identifier of the Docker account user.
- `docker_email` - (Optional) The email for Docker account user.
- `docker_password` - (Optional) The password for the account user identified above.
- `registry_type` - (Optional) Can be "DockerHub" or "Others" (Default "DockerHub").

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DockerEmail

The email for Docker account user.
- `docker_password` - (Optional) The password for the account user identified above.
- `registry_type` - (Optional) Can be "DockerHub" or "Others" (Default "DockerHub").

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DockerPassword

The password for the account user identified above.
- `registry_type` - (Optional) Can be "DockerHub" or "Others" (Default "DockerHub").

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DockerRegistry

The URL of the Docker registry. (Default: "https://index.docker.io/v1/")
- `docker_username` - (Optional) The identifier of the Docker account user.
- `docker_email` - (Optional) The email for Docker account user.
- `docker_password` - (Optional) The password for the account user identified above.
- `registry_type` - (Optional) Can be "DockerHub" or "Others" (Default "DockerHub").

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DockerUsername

The identifier of the Docker account user.
- `docker_email` - (Optional) The email for Docker account user.
- `docker_password` - (Optional) The password for the account user identified above.
- `registry_type` - (Optional) Can be "DockerHub" or "Others" (Default "DockerHub").

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

The project ID or project name.
- `service_endpoint_name` - (Required) The name you will use to refer to this service connection in task inputs.
- `description` - (Optional) The name you will use to refer to this service connection in task inputs.
- `docker_registry` - (Optional) The URL of the Docker registry. (Default: "https://index.docker.io/v1/")
- `docker_username` - (Optional) The identifier of the Docker account user.
- `docker_email` - (Optional) The email for Docker account user.
- `docker_password` - (Optional) The password for the account user identified above.
- `registry_type` - (Optional) Can be "DockerHub" or "Others" (Default "DockerHub").

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegistryType

Can be "DockerHub" or "Others" (Default "DockerHub").

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceEndpointName

The name you will use to refer to this service connection in task inputs.
- `description` - (Optional) The name you will use to refer to this service connection in task inputs.
- `docker_registry` - (Optional) The URL of the Docker registry. (Default: "https://index.docker.io/v1/")
- `docker_username` - (Optional) The identifier of the Docker account user.
- `docker_email` - (Optional) The email for Docker account user.
- `docker_password` - (Optional) The password for the account user identified above.
- `registry_type` - (Optional) Can be "DockerHub" or "Others" (Default "DockerHub").

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

#### DockerPasswordHash

Returns the <code>DockerPasswordHash</code> value.

#### Id

Returns the <code>Id</code> value.

