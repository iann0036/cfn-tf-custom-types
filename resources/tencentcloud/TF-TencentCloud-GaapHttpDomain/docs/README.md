# TF::TencentCloud::GaapHttpDomain

Provides a resource to create a forward domain of layer7 listener.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::TencentCloud::GaapHttpDomain",
    "Properties" : {
        "<a href="#basicauth" title="BasicAuth">BasicAuth</a>" : <i>Boolean</i>,
        "<a href="#basicauthid" title="BasicAuthId">BasicAuthId</a>" : <i>String</i>,
        "<a href="#certificateid" title="CertificateId">CertificateId</a>" : <i>String</i>,
        "<a href="#clientcertificateid" title="ClientCertificateId">ClientCertificateId</a>" : <i>String</i>,
        "<a href="#clientcertificateids" title="ClientCertificateIds">ClientCertificateIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#domain" title="Domain">Domain</a>" : <i>String</i>,
        "<a href="#gaapauth" title="GaapAuth">GaapAuth</a>" : <i>Boolean</i>,
        "<a href="#gaapauthid" title="GaapAuthId">GaapAuthId</a>" : <i>String</i>,
        "<a href="#listenerid" title="ListenerId">ListenerId</a>" : <i>String</i>,
        "<a href="#realserverauth" title="RealserverAuth">RealserverAuth</a>" : <i>Boolean</i>,
        "<a href="#realservercertificatedomain" title="RealserverCertificateDomain">RealserverCertificateDomain</a>" : <i>String</i>,
        "<a href="#realservercertificateid" title="RealserverCertificateId">RealserverCertificateId</a>" : <i>String</i>,
        "<a href="#realservercertificateids" title="RealserverCertificateIds">RealserverCertificateIds</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::TencentCloud::GaapHttpDomain
Properties:
    <a href="#basicauth" title="BasicAuth">BasicAuth</a>: <i>Boolean</i>
    <a href="#basicauthid" title="BasicAuthId">BasicAuthId</a>: <i>String</i>
    <a href="#certificateid" title="CertificateId">CertificateId</a>: <i>String</i>
    <a href="#clientcertificateid" title="ClientCertificateId">ClientCertificateId</a>: <i>String</i>
    <a href="#clientcertificateids" title="ClientCertificateIds">ClientCertificateIds</a>: <i>
      - String</i>
    <a href="#domain" title="Domain">Domain</a>: <i>String</i>
    <a href="#gaapauth" title="GaapAuth">GaapAuth</a>: <i>Boolean</i>
    <a href="#gaapauthid" title="GaapAuthId">GaapAuthId</a>: <i>String</i>
    <a href="#listenerid" title="ListenerId">ListenerId</a>: <i>String</i>
    <a href="#realserverauth" title="RealserverAuth">RealserverAuth</a>: <i>Boolean</i>
    <a href="#realservercertificatedomain" title="RealserverCertificateDomain">RealserverCertificateDomain</a>: <i>String</i>
    <a href="#realservercertificateid" title="RealserverCertificateId">RealserverCertificateId</a>: <i>String</i>
    <a href="#realservercertificateids" title="RealserverCertificateIds">RealserverCertificateIds</a>: <i>
      - String</i>
</pre>

## Properties

#### BasicAuth

Indicates whether basic authentication is enable, default value is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BasicAuthId

ID of the basic authentication.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateId

ID of the server certificate, default value is `default`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientCertificateId

It has been deprecated from version 1.26.0. Set `client_certificate_ids` instead. ID of the client certificate, default value is `default`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientCertificateIds

ID list of the poly client certificate.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domain

Forward domain of the layer7 listener.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GaapAuth

Indicates whether SSL certificate authentication is enable, default value is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GaapAuthId

ID of the SSL certificate.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ListenerId

ID of the layer7 listener.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RealserverAuth

Indicates whether realserver authentication is enable, default value is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RealserverCertificateDomain

CA certificate domain of the realserver.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RealserverCertificateId

It has been deprecated from version 1.28.0. Set `realserver_certificate_ids` instead. CA certificate ID of the realserver.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RealserverCertificateIds

CA certificate ID list of the realserver.

_Required_: No

_Type_: List of String

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

