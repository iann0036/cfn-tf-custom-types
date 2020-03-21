# Terraform::AWS::CloudfrontDistribution CustomOriginConfig

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#httpport" title="HttpPort">HttpPort</a>" : <i>Double</i>,
    "<a href="#httpsport" title="HttpsPort">HttpsPort</a>" : <i>Double</i>,
    "<a href="#originkeepalivetimeout" title="OriginKeepaliveTimeout">OriginKeepaliveTimeout</a>" : <i>Double</i>,
    "<a href="#originprotocolpolicy" title="OriginProtocolPolicy">OriginProtocolPolicy</a>" : <i>String</i>,
    "<a href="#originreadtimeout" title="OriginReadTimeout">OriginReadTimeout</a>" : <i>Double</i>,
    "<a href="#originsslprotocols" title="OriginSslProtocols">OriginSslProtocols</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#httpport" title="HttpPort">HttpPort</a>: <i>Double</i>
<a href="#httpsport" title="HttpsPort">HttpsPort</a>: <i>Double</i>
<a href="#originkeepalivetimeout" title="OriginKeepaliveTimeout">OriginKeepaliveTimeout</a>: <i>Double</i>
<a href="#originprotocolpolicy" title="OriginProtocolPolicy">OriginProtocolPolicy</a>: <i>String</i>
<a href="#originreadtimeout" title="OriginReadTimeout">OriginReadTimeout</a>: <i>Double</i>
<a href="#originsslprotocols" title="OriginSslProtocols">OriginSslProtocols</a>: <i>
      - String</i>
</pre>

## Properties

#### HttpPort

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpsPort

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OriginKeepaliveTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OriginProtocolPolicy

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OriginReadTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OriginSslProtocols

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

