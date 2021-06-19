# TF::AWS::Route53Record

Provides a Route53 record resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::Route53Record",
    "Properties" : {
        "<a href="#allowoverwrite" title="AllowOverwrite">AllowOverwrite</a>" : <i>Boolean</i>,
        "<a href="#healthcheckid" title="HealthCheckId">HealthCheckId</a>" : <i>String</i>,
        "<a href="#multivalueanswerroutingpolicy" title="MultivalueAnswerRoutingPolicy">MultivalueAnswerRoutingPolicy</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#records" title="Records">Records</a>" : <i>[ String, ... ]</i>,
        "<a href="#setidentifier" title="SetIdentifier">SetIdentifier</a>" : <i>String</i>,
        "<a href="#ttl" title="Ttl">Ttl</a>" : <i>Double</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#zoneid" title="ZoneId">ZoneId</a>" : <i>String</i>,
        "<a href="#alias" title="Alias">Alias</a>" : <i>[ <a href="aliasdefinition.md">AliasDefinition</a>, ... ]</i>,
        "<a href="#failoverroutingpolicy" title="FailoverRoutingPolicy">FailoverRoutingPolicy</a>" : <i>[ <a href="failoverroutingpolicydefinition.md">FailoverRoutingPolicyDefinition</a>, ... ]</i>,
        "<a href="#geolocationroutingpolicy" title="GeolocationRoutingPolicy">GeolocationRoutingPolicy</a>" : <i>[ <a href="geolocationroutingpolicydefinition.md">GeolocationRoutingPolicyDefinition</a>, ... ]</i>,
        "<a href="#latencyroutingpolicy" title="LatencyRoutingPolicy">LatencyRoutingPolicy</a>" : <i>[ <a href="latencyroutingpolicydefinition.md">LatencyRoutingPolicyDefinition</a>, ... ]</i>,
        "<a href="#weightedroutingpolicy" title="WeightedRoutingPolicy">WeightedRoutingPolicy</a>" : <i>[ <a href="weightedroutingpolicydefinition.md">WeightedRoutingPolicyDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::Route53Record
Properties:
    <a href="#allowoverwrite" title="AllowOverwrite">AllowOverwrite</a>: <i>Boolean</i>
    <a href="#healthcheckid" title="HealthCheckId">HealthCheckId</a>: <i>String</i>
    <a href="#multivalueanswerroutingpolicy" title="MultivalueAnswerRoutingPolicy">MultivalueAnswerRoutingPolicy</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#records" title="Records">Records</a>: <i>
      - String</i>
    <a href="#setidentifier" title="SetIdentifier">SetIdentifier</a>: <i>String</i>
    <a href="#ttl" title="Ttl">Ttl</a>: <i>Double</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#zoneid" title="ZoneId">ZoneId</a>: <i>String</i>
    <a href="#alias" title="Alias">Alias</a>: <i>
      - <a href="aliasdefinition.md">AliasDefinition</a></i>
    <a href="#failoverroutingpolicy" title="FailoverRoutingPolicy">FailoverRoutingPolicy</a>: <i>
      - <a href="failoverroutingpolicydefinition.md">FailoverRoutingPolicyDefinition</a></i>
    <a href="#geolocationroutingpolicy" title="GeolocationRoutingPolicy">GeolocationRoutingPolicy</a>: <i>
      - <a href="geolocationroutingpolicydefinition.md">GeolocationRoutingPolicyDefinition</a></i>
    <a href="#latencyroutingpolicy" title="LatencyRoutingPolicy">LatencyRoutingPolicy</a>: <i>
      - <a href="latencyroutingpolicydefinition.md">LatencyRoutingPolicyDefinition</a></i>
    <a href="#weightedroutingpolicy" title="WeightedRoutingPolicy">WeightedRoutingPolicy</a>: <i>
      - <a href="weightedroutingpolicydefinition.md">WeightedRoutingPolicyDefinition</a></i>
</pre>

## Properties

#### AllowOverwrite

Allow creation of this record in Terraform to overwrite an existing record, if any. This does not affect the ability to update the record in Terraform and does not prevent other resources within Terraform or manual Route 53 changes outside Terraform from overwriting this record. `false` by default. This configuration is not recommended for most environments.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckId

The health check the record should be associated with.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MultivalueAnswerRoutingPolicy

Set to `true` to indicate a multivalue answer routing policy. Conflicts with any other routing policy.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Records

A string list of records. To specify a single record value longer than 255 characters such as a TXT record for DKIM, add `\"\"` inside the Terraform configuration string (e.g. `"first255characters\"\"morecharacters"`).

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SetIdentifier

Unique identifier to differentiate records with routing policies from one another. Required if using `failover`, `geolocation`, `latency`, or `weighted` routing policies documented below.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ttl

The TTL of the record.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

`PRIMARY` or `SECONDARY`. A `PRIMARY` record will be served if its healthcheck is passing, otherwise the `SECONDARY` will be served. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZoneId

Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See [`resource_elb.zone_id`](/docs/providers/aws/r/elb.html#zone_id) for example.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Alias

_Required_: No

_Type_: List of <a href="aliasdefinition.md">AliasDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FailoverRoutingPolicy

_Required_: No

_Type_: List of <a href="failoverroutingpolicydefinition.md">FailoverRoutingPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GeolocationRoutingPolicy

_Required_: No

_Type_: List of <a href="geolocationroutingpolicydefinition.md">GeolocationRoutingPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LatencyRoutingPolicy

_Required_: No

_Type_: List of <a href="latencyroutingpolicydefinition.md">LatencyRoutingPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WeightedRoutingPolicy

_Required_: No

_Type_: List of <a href="weightedroutingpolicydefinition.md">WeightedRoutingPolicyDefinition</a>

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

Returns the <code>Fqdn</code> value.

#### Id

Returns the <code>Id</code> value.

