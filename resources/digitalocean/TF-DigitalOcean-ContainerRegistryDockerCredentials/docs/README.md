# TF::DigitalOcean::ContainerRegistryDockerCredentials

Get Docker credentials for your DigitalOcean container registry.

An error is triggered if the provided container registry name does not exist.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::DigitalOcean::ContainerRegistryDockerCredentials",
    "Properties" : {
        "<a href="#expiryseconds" title="ExpirySeconds">ExpirySeconds</a>" : <i>Double</i>,
        "<a href="#registryname" title="RegistryName">RegistryName</a>" : <i>String</i>,
        "<a href="#write" title="Write">Write</a>" : <i>Boolean</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::DigitalOcean::ContainerRegistryDockerCredentials
Properties:
    <a href="#expiryseconds" title="ExpirySeconds">ExpirySeconds</a>: <i>Double</i>
    <a href="#registryname" title="RegistryName">RegistryName</a>: <i>String</i>
    <a href="#write" title="Write">Write</a>: <i>Boolean</i>
</pre>

## Properties

#### ExpirySeconds

The amount of time to pass before the Docker credentials expire in seconds. Defaults to 1576800000, or roughly 50 years. Must be greater than 0 and less than 1576800000.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegistryName

The name of the container registry.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Write

Allow for write access to the container registry. Defaults to false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CredentialExpirationTime

Returns the <code>CredentialExpirationTime</code> value.

#### DockerCredentials

Returns the <code>DockerCredentials</code> value.

#### Id

Returns the <code>Id</code> value.

