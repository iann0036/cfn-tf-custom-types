# Terraform::AWS::Route53Record

CloudFormation equivalent of aws_route53_record

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::Route53Record",
    "Properties" : {
        "<a href="#allowoverwrite" title="AllowOverwrite">AllowOverwrite</a>" : <i>Boolean</i>,
        "<a href="#healthcheckid" title="HealthCheckId">HealthCheckId</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#multivalueanswerroutingpolicy" title="MultivalueAnswerRoutingPolicy">MultivalueAnswerRoutingPolicy</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#records" title="Records">Records</a>" : <i>[ String, ... ]</i>,
        "<a href="#setidentifier" title="SetIdentifier">SetIdentifier</a>" : <i>String</i>,
        "<a href="#ttl" title="Ttl">Ttl</a>" : <i>Double</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#zoneid" title="ZoneId">ZoneId</a>" : <i>String</i>,
        "<a href="#alias" title="Alias">Alias</a>" : <i>[ &lt;a href=&#34;alias.md&#34;&gt;Alias&lt;/a&gt;, ... ]</i>,
        "<a href="#failoverroutingpolicy" title="FailoverRoutingPolicy">FailoverRoutingPolicy</a>" : <i>[ &lt;a href=&#34;failoverroutingpolicy.md&#34;&gt;FailoverRoutingPolicy&lt;/a&gt;, ... ]</i>,
        "<a href="#geolocationroutingpolicy" title="GeolocationRoutingPolicy">GeolocationRoutingPolicy</a>" : <i>[ &lt;a href=&#34;geolocationroutingpolicy.md&#34;&gt;GeolocationRoutingPolicy&lt;/a&gt;, ... ]</i>,
        "<a href="#latencyroutingpolicy" title="LatencyRoutingPolicy">LatencyRoutingPolicy</a>" : <i>[ &lt;a href=&#34;latencyroutingpolicy.md&#34;&gt;LatencyRoutingPolicy&lt;/a&gt;, ... ]</i>,
        "<a href="#weightedroutingpolicy" title="WeightedRoutingPolicy">WeightedRoutingPolicy</a>" : <i>[ &lt;a href=&#34;weightedroutingpolicy.md&#34;&gt;WeightedRoutingPolicy&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::Route53Record
Properties:
    <a href="#allowoverwrite" title="AllowOverwrite">AllowOverwrite</a>: <i>Boolean</i>
    <a href="#healthcheckid" title="HealthCheckId">HealthCheckId</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#multivalueanswerroutingpolicy" title="MultivalueAnswerRoutingPolicy">MultivalueAnswerRoutingPolicy</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#records" title="Records">Records</a>: <i>
      - String</i>
    <a href="#setidentifier" title="SetIdentifier">SetIdentifier</a>: <i>String</i>
    <a href="#ttl" title="Ttl">Ttl</a>: <i>Double</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#zoneid" title="ZoneId">ZoneId</a>: <i>String</i>
    <a href="#alias" title="Alias">Alias</a>: <i>
      - &lt;a href=&#34;alias.md&#34;&gt;Alias&lt;/a&gt;</i>
    <a href="#failoverroutingpolicy" title="FailoverRoutingPolicy">FailoverRoutingPolicy</a>: <i>
      - &lt;a href=&#34;failoverroutingpolicy.md&#34;&gt;FailoverRoutingPolicy&lt;/a&gt;</i>
    <a href="#geolocationroutingpolicy" title="GeolocationRoutingPolicy">GeolocationRoutingPolicy</a>: <i>
      - &lt;a href=&#34;geolocationroutingpolicy.md&#34;&gt;GeolocationRoutingPolicy&lt;/a&gt;</i>
    <a href="#latencyroutingpolicy" title="LatencyRoutingPolicy">LatencyRoutingPolicy</a>: <i>
      - &lt;a href=&#34;latencyroutingpolicy.md&#34;&gt;LatencyRoutingPolicy&lt;/a&gt;</i>
    <a href="#weightedroutingpolicy" title="WeightedRoutingPolicy">WeightedRoutingPolicy</a>: <i>
      - &lt;a href=&#34;weightedroutingpolicy.md&#34;&gt;WeightedRoutingPolicy&lt;/a&gt;</i>
</pre>

## Properties

#### AllowOverwrite

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MultivalueAnswerRoutingPolicy

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Records

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SetIdentifier

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ttl

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZoneId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Alias

_Required_: No

_Type_: List of &lt;a href=&#34;alias.md&#34;&gt;Alias&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FailoverRoutingPolicy

_Required_: No

_Type_: List of &lt;a href=&#34;failoverroutingpolicy.md&#34;&gt;FailoverRoutingPolicy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GeolocationRoutingPolicy

_Required_: No

_Type_: List of &lt;a href=&#34;geolocationroutingpolicy.md&#34;&gt;GeolocationRoutingPolicy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LatencyRoutingPolicy

_Required_: No

_Type_: List of &lt;a href=&#34;latencyroutingpolicy.md&#34;&gt;LatencyRoutingPolicy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WeightedRoutingPolicy

_Required_: No

_Type_: List of &lt;a href=&#34;weightedroutingpolicy.md&#34;&gt;WeightedRoutingPolicy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Fqdn

Returns the &lt;code&gt;Fqdn&lt;/code&gt; value.

