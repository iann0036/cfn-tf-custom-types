# TF::AWS::Apigatewayv2DomainName DomainNameConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#certificatearn" title="CertificateArn">CertificateArn</a>" : <i>String</i>,
    "<a href="#endpointtype" title="EndpointType">EndpointType</a>" : <i>String</i>,
    "<a href="#securitypolicy" title="SecurityPolicy">SecurityPolicy</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#certificatearn" title="CertificateArn">CertificateArn</a>: <i>String</i>
<a href="#endpointtype" title="EndpointType">EndpointType</a>: <i>String</i>
<a href="#securitypolicy" title="SecurityPolicy">SecurityPolicy</a>: <i>String</i>
</pre>

## Properties

#### CertificateArn

The ARN of an AWS-managed certificate that will be used by the endpoint for the domain name. AWS Certificate Manager is the only supported source.
Use the [`aws_acm_certificate`](/docs/providers/aws/r/acm_certificate.html) resource to configure an ACM certificate.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndpointType

The endpoint type. Valid values: `REGIONAL`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityPolicy

The Transport Layer Security (TLS) version of the [security policy](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-custom-domain-tls-version.html) for the domain name. Valid values: `TLS_1_2`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

