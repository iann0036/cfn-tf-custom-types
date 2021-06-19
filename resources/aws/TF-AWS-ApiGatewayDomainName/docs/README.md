# TF::AWS::ApiGatewayDomainName

Registers a custom domain name for use with AWS API Gateway. Additional information about this functionality
can be found in the [API Gateway Developer Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html).

This resource just establishes ownership of and the TLS settings for
a particular domain name. An API can be attached to a particular path
under the registered domain name using
[the `aws_api_gateway_base_path_mapping` resource](api_gateway_base_path_mapping.html).

API Gateway domains can be defined as either 'edge-optimized' or 'regional'.  In an edge-optimized configuration,
API Gateway internally creates and manages a CloudFront distribution to route requests on the given hostname. In
addition to this resource it's necessary to create a DNS record corresponding to the given domain name which is an alias
(either Route53 alias or traditional CNAME) to the Cloudfront domain name exported in the `cloudfront_domain_name`
attribute.

In a regional configuration,...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::ApiGatewayDomainName",
    "Properties" : {
        "<a href="#certificatearn" title="CertificateArn">CertificateArn</a>" : <i>String</i>,
        "<a href="#certificatebody" title="CertificateBody">CertificateBody</a>" : <i>String</i>,
        "<a href="#certificatechain" title="CertificateChain">CertificateChain</a>" : <i>String</i>,
        "<a href="#certificatename" title="CertificateName">CertificateName</a>" : <i>String</i>,
        "<a href="#certificateprivatekey" title="CertificatePrivateKey">CertificatePrivateKey</a>" : <i>String</i>,
        "<a href="#domainname" title="DomainName">DomainName</a>" : <i>String</i>,
        "<a href="#regionalcertificatearn" title="RegionalCertificateArn">RegionalCertificateArn</a>" : <i>String</i>,
        "<a href="#regionalcertificatename" title="RegionalCertificateName">RegionalCertificateName</a>" : <i>String</i>,
        "<a href="#securitypolicy" title="SecurityPolicy">SecurityPolicy</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#endpointconfiguration" title="EndpointConfiguration">EndpointConfiguration</a>" : <i>[ <a href="endpointconfigurationdefinition.md">EndpointConfigurationDefinition</a>, ... ]</i>,
        "<a href="#mutualtlsauthentication" title="MutualTlsAuthentication">MutualTlsAuthentication</a>" : <i>[ <a href="mutualtlsauthenticationdefinition.md">MutualTlsAuthenticationDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::ApiGatewayDomainName
Properties:
    <a href="#certificatearn" title="CertificateArn">CertificateArn</a>: <i>String</i>
    <a href="#certificatebody" title="CertificateBody">CertificateBody</a>: <i>String</i>
    <a href="#certificatechain" title="CertificateChain">CertificateChain</a>: <i>String</i>
    <a href="#certificatename" title="CertificateName">CertificateName</a>: <i>String</i>
    <a href="#certificateprivatekey" title="CertificatePrivateKey">CertificatePrivateKey</a>: <i>String</i>
    <a href="#domainname" title="DomainName">DomainName</a>: <i>String</i>
    <a href="#regionalcertificatearn" title="RegionalCertificateArn">RegionalCertificateArn</a>: <i>String</i>
    <a href="#regionalcertificatename" title="RegionalCertificateName">RegionalCertificateName</a>: <i>String</i>
    <a href="#securitypolicy" title="SecurityPolicy">SecurityPolicy</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#endpointconfiguration" title="EndpointConfiguration">EndpointConfiguration</a>: <i>
      - <a href="endpointconfigurationdefinition.md">EndpointConfigurationDefinition</a></i>
    <a href="#mutualtlsauthentication" title="MutualTlsAuthentication">MutualTlsAuthentication</a>: <i>
      - <a href="mutualtlsauthenticationdefinition.md">MutualTlsAuthenticationDefinition</a></i>
</pre>

## Properties

#### CertificateArn

The ARN for an AWS-managed certificate. AWS Certificate Manager is the only supported source. Used when an edge-optimized domain name is desired. Conflicts with `certificate_name`, `certificate_body`, `certificate_chain`, `certificate_private_key`, `regional_certificate_arn`, and `regional_certificate_name`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateBody

The certificate issued for the domain name
being registered, in PEM format. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`, `regional_certificate_arn`, and
`regional_certificate_name`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateChain

The certificate for the CA that issued the
certificate, along with any intermediate CA certificates required to
create an unbroken chain to a certificate trusted by the intended API clients. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`,
`regional_certificate_arn`, and `regional_certificate_name`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateName

The unique name to use when registering this
certificate as an IAM server certificate. Conflicts with `certificate_arn`, `regional_certificate_arn`, and
`regional_certificate_name`. Required if `certificate_arn` is not set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificatePrivateKey

The private key associated with the
domain certificate given in `certificate_body`. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`, `regional_certificate_arn`, and `regional_certificate_name`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainName

The fully-qualified domain name to register.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegionalCertificateArn

The ARN for an AWS-managed certificate. AWS Certificate Manager is the only supported source. Used when a regional domain name is desired. Conflicts with `certificate_arn`, `certificate_name`, `certificate_body`, `certificate_chain`, and `certificate_private_key`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegionalCertificateName

The user-friendly name of the certificate that will be used by regional endpoint for this domain name. Conflicts with `certificate_arn`, `certificate_name`, `certificate_body`, `certificate_chain`, and
`certificate_private_key`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityPolicy

The Transport Layer Security (TLS) version + cipher suite for this DomainName. The valid values are `TLS_1_0` and `TLS_1_2`. Must be configured to perform drift detection.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Key-value map of resource tags. If configured with a provider [`default_tags` configuration block](/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsAll

_Required_: No

_Type_: List of <a href="tagsalldefinition.md">TagsAllDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndpointConfiguration

_Required_: No

_Type_: List of <a href="endpointconfigurationdefinition.md">EndpointConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MutualTlsAuthentication

_Required_: No

_Type_: List of <a href="mutualtlsauthenticationdefinition.md">MutualTlsAuthenticationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### CertificateUploadDate

Returns the <code>CertificateUploadDate</code> value.

#### CloudfrontDomainName

Returns the <code>CloudfrontDomainName</code> value.

#### CloudfrontZoneId

Returns the <code>CloudfrontZoneId</code> value.

#### Id

Returns the <code>Id</code> value.

#### RegionalDomainName

Returns the <code>RegionalDomainName</code> value.

#### RegionalZoneId

Returns the <code>RegionalZoneId</code> value.

