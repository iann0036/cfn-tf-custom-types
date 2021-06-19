# TF::Gridscale::Loadbalancer ForwardingRuleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#certificateuuid" title="CertificateUuid">CertificateUuid</a>" : <i>String</i>,
    "<a href="#letsencryptssl" title="LetsencryptSsl">LetsencryptSsl</a>" : <i>String</i>,
    "<a href="#listenport" title="ListenPort">ListenPort</a>" : <i>Double</i>,
    "<a href="#mode" title="Mode">Mode</a>" : <i>String</i>,
    "<a href="#targetport" title="TargetPort">TargetPort</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#certificateuuid" title="CertificateUuid">CertificateUuid</a>: <i>String</i>
<a href="#letsencryptssl" title="LetsencryptSsl">LetsencryptSsl</a>: <i>String</i>
<a href="#listenport" title="ListenPort">ListenPort</a>: <i>Double</i>
<a href="#mode" title="Mode">Mode</a>: <i>String</i>
<a href="#targetport" title="TargetPort">TargetPort</a>: <i>Double</i>
</pre>

## Properties

#### CertificateUuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LetsencryptSsl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ListenPort

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mode

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetPort

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

