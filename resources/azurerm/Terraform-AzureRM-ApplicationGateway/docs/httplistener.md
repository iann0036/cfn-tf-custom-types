# Terraform::AzureRM::ApplicationGateway HttpListener

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#frontendipconfigurationname" title="FrontendIpConfigurationName">FrontendIpConfigurationName</a>" : <i>String</i>,
    "<a href="#frontendportname" title="FrontendPortName">FrontendPortName</a>" : <i>String</i>,
    "<a href="#hostname" title="HostName">HostName</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
    "<a href="#requiresni" title="RequireSni">RequireSni</a>" : <i>Boolean</i>,
    "<a href="#sslcertificatename" title="SslCertificateName">SslCertificateName</a>" : <i>String</i>,
    "<a href="#customerrorconfiguration" title="CustomErrorConfiguration">CustomErrorConfiguration</a>" : <i>[ <a href="httplistener-customerrorconfiguration.md">CustomErrorConfiguration</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#frontendipconfigurationname" title="FrontendIpConfigurationName">FrontendIpConfigurationName</a>: <i>String</i>
<a href="#frontendportname" title="FrontendPortName">FrontendPortName</a>: <i>String</i>
<a href="#hostname" title="HostName">HostName</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
<a href="#requiresni" title="RequireSni">RequireSni</a>: <i>Boolean</i>
<a href="#sslcertificatename" title="SslCertificateName">SslCertificateName</a>: <i>String</i>
<a href="#customerrorconfiguration" title="CustomErrorConfiguration">CustomErrorConfiguration</a>: <i>
      - <a href="httplistener-customerrorconfiguration.md">CustomErrorConfiguration</a></i>
</pre>

## Properties

#### FrontendIpConfigurationName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FrontendPortName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequireSni

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslCertificateName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomErrorConfiguration

_Required_: No

_Type_: List of <a href="httplistener-customerrorconfiguration.md">CustomErrorConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

