# TF::Consul::License

~> **NOTE:** This feature requires [Consul Enterprise](https://www.consul.io/docs/enterprise/index.html).

The `consul_license` resource provides datacenter-level management of
the Consul Enterprise license. If ACLs are enabled then a token with operator
privileges may be required in order to use this command.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Consul::License",
    "Properties" : {
        "<a href="#datacenter" title="Datacenter">Datacenter</a>" : <i>String</i>,
        "<a href="#license" title="License">License</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Consul::License
Properties:
    <a href="#datacenter" title="Datacenter">Datacenter</a>: <i>String</i>
    <a href="#license" title="License">License</a>: <i>String</i>
</pre>

## Properties

#### Datacenter

The datacenter to use. This overrides the
agent's default datacenter and the datacenter in the provider setup.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### License

The Consul license to use.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CustomerId

Returns the <code>CustomerId</code> value.

#### ExpirationTime

Returns the <code>ExpirationTime</code> value.

#### Features

Returns the <code>Features</code> value.

#### Id

Returns the <code>Id</code> value.

#### InstallationId

Returns the <code>InstallationId</code> value.

#### IssueTime

Returns the <code>IssueTime</code> value.

#### LicenseId

Returns the <code>LicenseId</code> value.

#### Product

Returns the <code>Product</code> value.

#### StartTime

Returns the <code>StartTime</code> value.

#### Valid

Returns the <code>Valid</code> value.

#### Warnings

Returns the <code>Warnings</code> value.

