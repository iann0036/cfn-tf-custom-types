# Terraform::TencentCloud::SslCertificate

Provides a resource to create a SSL certificate.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::TencentCloud::SslCertificate",
    "Properties" : {
        "<a href="#cert" title="Cert">Cert</a>" : <i>String</i>,
        "<a href="#key" title="Key">Key</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>Double</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::TencentCloud::SslCertificate
Properties:
    <a href="#cert" title="Cert">Cert</a>: <i>String</i>
    <a href="#key" title="Key">Key</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>Double</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### Cert

Content of the SSL certificate. Not allowed newline at the start and end.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Key

Key of the SSL certificate and required when certificate type is `SVR`. Not allowed newline at the start and end.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the SSL certificate.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

Project ID of the SSL certificate. Default is `0`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Type of the SSL certificate. Available values includes: `CA` and `SVR`.

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

#### BeginTime

Returns the <code>BeginTime</code> value.

#### CreateTime

Returns the <code>CreateTime</code> value.

#### Domain

Returns the <code>Domain</code> value.

#### EndTime

Returns the <code>EndTime</code> value.

#### Id

Returns the <code>Id</code> value.

#### ProductZhName

Returns the <code>ProductZhName</code> value.

#### Status

Returns the <code>Status</code> value.

#### SubjectNames

Returns the <code>SubjectNames</code> value.

