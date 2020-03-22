# Terraform::OpenStack::IdentityEndpointV3

Manages a V3 Endpoint resource within OpenStack Keystone.

~> **Note:** This usually requires admin privileges.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OpenStack::IdentityEndpointV3",
    "Properties" : {
        "<a href="#endpointregion" title="EndpointRegion">EndpointRegion</a>" : <i>String</i>,
        "<a href="#interface" title="Interface">Interface</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#serviceid" title="ServiceId">ServiceId</a>" : <i>String</i>,
        "<a href="#url" title="Url">Url</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OpenStack::IdentityEndpointV3
Properties:
    <a href="#endpointregion" title="EndpointRegion">EndpointRegion</a>: <i>String</i>
    <a href="#interface" title="Interface">Interface</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#serviceid" title="ServiceId">ServiceId</a>: <i>String</i>
    <a href="#url" title="Url">Url</a>: <i>String</i>
</pre>

## Properties

#### EndpointRegion

The endpoint region. The `region` and
`endpoint_region` can be different.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface

The endpoint interface. Valid values are `public`,
`internal` and `admin`. Default value is `public`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The endpoint name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The region in which to obtain the V3 Keystone client.
If omitted, the `region` argument of the provider is used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceId

The endpoint service ID.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Url

The endpoint url.

_Required_: Yes

_Type_: String

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

#### ServiceName

Returns the <code>ServiceName</code> value.

#### ServiceType

Returns the <code>ServiceType</code> value.

