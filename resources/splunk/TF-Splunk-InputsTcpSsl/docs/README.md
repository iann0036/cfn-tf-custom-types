# TF::Splunk::InputsTcpSsl

Access or update the SSL configuration for the host.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Splunk::InputsTcpSsl",
    "Properties" : {
        "<a href="#disabled" title="Disabled">Disabled</a>" : <i>Boolean</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#requireclientcert" title="RequireClientCert">RequireClientCert</a>" : <i>Boolean</i>,
        "<a href="#rootca" title="RootCa">RootCa</a>" : <i>String</i>,
        "<a href="#servercert" title="ServerCert">ServerCert</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Splunk::InputsTcpSsl
Properties:
    <a href="#disabled" title="Disabled">Disabled</a>: <i>Boolean</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#requireclientcert" title="RequireClientCert">RequireClientCert</a>: <i>Boolean</i>
    <a href="#rootca" title="RootCa">RootCa</a>: <i>String</i>
    <a href="#servercert" title="ServerCert">ServerCert</a>: <i>String</i>
</pre>

## Properties

#### Disabled

Indicates if input is disabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

Server certificate password, if any.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequireClientCert

Determines whether a client must authenticate.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RootCa

Certificate authority list (root file).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerCert

Full path to the server certificate.

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

#### Id

Returns the <code>Id</code> value.

