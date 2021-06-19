# TF::MongoDBAtlas::X509AuthenticationDatabaseUser

`mongodbatlas_x509_authentication_database_user` provides a X509 Authentication Database User resource. The mongodbatlas_x509_authentication_database_user resource lets you manage MongoDB users who authenticate using X.509 certificates. You can manage these X.509 certificates or let Atlas do it for you.

| Management  | Description  |
|---|---|
| Atlas  | Atlas manages your Certificate Authority and can generate certificates for your MongoDB users. No additional X.509 configuration is required.  |
| Customer  |  You must provide a Certificate Authority and generate certificates for your MongoDB users. |

-> **NOTE:** Groups and projects are synonymous terms. You may find group_id in the official documentation.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::MongoDBAtlas::X509AuthenticationDatabaseUser",
    "Properties" : {
        "<a href="#customerx509cas" title="CustomerX509Cas">CustomerX509Cas</a>" : <i>String</i>,
        "<a href="#monthsuntilexpiration" title="MonthsUntilExpiration">MonthsUntilExpiration</a>" : <i>Double</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>,
        "<a href="#username" title="Username">Username</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::MongoDBAtlas::X509AuthenticationDatabaseUser
Properties:
    <a href="#customerx509cas" title="CustomerX509Cas">CustomerX509Cas</a>: <i>String</i>
    <a href="#monthsuntilexpiration" title="MonthsUntilExpiration">MonthsUntilExpiration</a>: <i>Double</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
    <a href="#username" title="Username">Username</a>: <i>String</i>
</pre>

## Properties

#### CustomerX509Cas

PEM string containing one or more customer CAs for database user authentication.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MonthsUntilExpiration

A number of months that the created certificate is valid for before expiry, up to 24 months. By default is 3.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

Identifier for the Atlas project associated with the X.509 configuration.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Username

Username of the database user to create a certificate for.

_Required_: No

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

#### Certificates

Returns the <code>Certificates</code> value.

#### CurrentCertificate

Returns the <code>CurrentCertificate</code> value.

#### Id

Returns the <code>Id</code> value.

