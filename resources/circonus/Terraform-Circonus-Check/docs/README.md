# Terraform::Circonus::Check

CloudFormation equivalent of circonus_check

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Circonus::Check",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#active" title="Active">Active</a>" : <i>Boolean</i>,
        "<a href="#checkbycollector" title="CheckByCollector">CheckByCollector</a>" : <i>[ &lt;a href=&#34;checkbycollector.md&#34;&gt;CheckByCollector&lt;/a&gt;, ... ]</i>,
        "<a href="#checkid" title="CheckId">CheckId</a>" : <i>String</i>,
        "<a href="#checks" title="Checks">Checks</a>" : <i>[ String, ... ]</i>,
        "<a href="#created" title="Created">Created</a>" : <i>Double</i>,
        "<a href="#lastmodified" title="LastModified">LastModified</a>" : <i>Double</i>,
        "<a href="#lastmodifiedby" title="LastModifiedBy">LastModifiedBy</a>" : <i>String</i>,
        "<a href="#metriclimit" title="MetricLimit">MetricLimit</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#notes" title="Notes">Notes</a>" : <i>String</i>,
        "<a href="#period" title="Period">Period</a>" : <i>String</i>,
        "<a href="#reverseconnecturls" title="ReverseConnectUrls">ReverseConnectUrls</a>" : <i>[ String, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#target" title="Target">Target</a>" : <i>String</i>,
        "<a href="#timeout" title="Timeout">Timeout</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#uuids" title="Uuids">Uuids</a>" : <i>[ String, ... ]</i>,
        "<a href="#caql" title="Caql">Caql</a>" : <i>[ &lt;a href=&#34;caql.md&#34;&gt;Caql&lt;/a&gt;, ... ]</i>,
        "<a href="#cloudwatch" title="Cloudwatch">Cloudwatch</a>" : <i>[ &lt;a href=&#34;cloudwatch.md&#34;&gt;Cloudwatch&lt;/a&gt;, ... ]</i>,
        "<a href="#collector" title="Collector">Collector</a>" : <i>[ &lt;a href=&#34;collector.md&#34;&gt;Collector&lt;/a&gt;, ... ]</i>,
        "<a href="#consul" title="Consul">Consul</a>" : <i>[ &lt;a href=&#34;consul.md&#34;&gt;Consul&lt;/a&gt;, ... ]</i>,
        "<a href="#dns" title="Dns">Dns</a>" : <i>[ &lt;a href=&#34;dns.md&#34;&gt;Dns&lt;/a&gt;, ... ]</i>,
        "<a href="#external" title="External">External</a>" : <i>[ &lt;a href=&#34;external.md&#34;&gt;External&lt;/a&gt;, ... ]</i>,
        "<a href="#http" title="Http">Http</a>" : <i>[ &lt;a href=&#34;http.md&#34;&gt;Http&lt;/a&gt;, ... ]</i>,
        "<a href="#httptrap" title="Httptrap">Httptrap</a>" : <i>[ &lt;a href=&#34;httptrap.md&#34;&gt;Httptrap&lt;/a&gt;, ... ]</i>,
        "<a href="#icmpping" title="IcmpPing">IcmpPing</a>" : <i>[ &lt;a href=&#34;icmpping.md&#34;&gt;IcmpPing&lt;/a&gt;, ... ]</i>,
        "<a href="#jmx" title="Jmx">Jmx</a>" : <i>[ &lt;a href=&#34;jmx.md&#34;&gt;Jmx&lt;/a&gt;, ... ]</i>,
        "<a href="#json" title="Json">Json</a>" : <i>[ &lt;a href=&#34;json.md&#34;&gt;Json&lt;/a&gt;, ... ]</i>,
        "<a href="#memcached" title="Memcached">Memcached</a>" : <i>[ &lt;a href=&#34;memcached.md&#34;&gt;Memcached&lt;/a&gt;, ... ]</i>,
        "<a href="#metric" title="Metric">Metric</a>" : <i>[ &lt;a href=&#34;metric.md&#34;&gt;Metric&lt;/a&gt;, ... ]</i>,
        "<a href="#metricfilter" title="MetricFilter">MetricFilter</a>" : <i>[ &lt;a href=&#34;metricfilter.md&#34;&gt;MetricFilter&lt;/a&gt;, ... ]</i>,
        "<a href="#mysql" title="Mysql">Mysql</a>" : <i>[ &lt;a href=&#34;mysql.md&#34;&gt;Mysql&lt;/a&gt;, ... ]</i>,
        "<a href="#postgresql" title="Postgresql">Postgresql</a>" : <i>[ &lt;a href=&#34;postgresql.md&#34;&gt;Postgresql&lt;/a&gt;, ... ]</i>,
        "<a href="#promtext" title="Promtext">Promtext</a>" : <i>[ &lt;a href=&#34;promtext.md&#34;&gt;Promtext&lt;/a&gt;, ... ]</i>,
        "<a href="#redis" title="Redis">Redis</a>" : <i>[ &lt;a href=&#34;redis.md&#34;&gt;Redis&lt;/a&gt;, ... ]</i>,
        "<a href="#snmp" title="Snmp">Snmp</a>" : <i>[ &lt;a href=&#34;snmp.md&#34;&gt;Snmp&lt;/a&gt;, ... ]</i>,
        "<a href="#statsd" title="Statsd">Statsd</a>" : <i>[ &lt;a href=&#34;statsd.md&#34;&gt;Statsd&lt;/a&gt;, ... ]</i>,
        "<a href="#tcp" title="Tcp">Tcp</a>" : <i>[ &lt;a href=&#34;tcp.md&#34;&gt;Tcp&lt;/a&gt;, ... ]</i>,
        "<a href="#mbeanproperties" title="MbeanProperties">MbeanProperties</a>" : <i>[ &lt;a href=&#34;mbeanproperties.md&#34;&gt;MbeanProperties&lt;/a&gt;, ... ]</i>,
        "<a href="#oid" title="Oid">Oid</a>" : <i>[ &lt;a href=&#34;oid.md&#34;&gt;Oid&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Circonus::Check
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#active" title="Active">Active</a>: <i>Boolean</i>
    <a href="#checkbycollector" title="CheckByCollector">CheckByCollector</a>: <i>
      - &lt;a href=&#34;checkbycollector.md&#34;&gt;CheckByCollector&lt;/a&gt;</i>
    <a href="#checkid" title="CheckId">CheckId</a>: <i>String</i>
    <a href="#checks" title="Checks">Checks</a>: <i>
      - String</i>
    <a href="#created" title="Created">Created</a>: <i>Double</i>
    <a href="#lastmodified" title="LastModified">LastModified</a>: <i>Double</i>
    <a href="#lastmodifiedby" title="LastModifiedBy">LastModifiedBy</a>: <i>String</i>
    <a href="#metriclimit" title="MetricLimit">MetricLimit</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#notes" title="Notes">Notes</a>: <i>String</i>
    <a href="#period" title="Period">Period</a>: <i>String</i>
    <a href="#reverseconnecturls" title="ReverseConnectUrls">ReverseConnectUrls</a>: <i>
      - String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#target" title="Target">Target</a>: <i>String</i>
    <a href="#timeout" title="Timeout">Timeout</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#uuids" title="Uuids">Uuids</a>: <i>
      - String</i>
    <a href="#caql" title="Caql">Caql</a>: <i>
      - &lt;a href=&#34;caql.md&#34;&gt;Caql&lt;/a&gt;</i>
    <a href="#cloudwatch" title="Cloudwatch">Cloudwatch</a>: <i>
      - &lt;a href=&#34;cloudwatch.md&#34;&gt;Cloudwatch&lt;/a&gt;</i>
    <a href="#collector" title="Collector">Collector</a>: <i>
      - &lt;a href=&#34;collector.md&#34;&gt;Collector&lt;/a&gt;</i>
    <a href="#consul" title="Consul">Consul</a>: <i>
      - &lt;a href=&#34;consul.md&#34;&gt;Consul&lt;/a&gt;</i>
    <a href="#dns" title="Dns">Dns</a>: <i>
      - &lt;a href=&#34;dns.md&#34;&gt;Dns&lt;/a&gt;</i>
    <a href="#external" title="External">External</a>: <i>
      - &lt;a href=&#34;external.md&#34;&gt;External&lt;/a&gt;</i>
    <a href="#http" title="Http">Http</a>: <i>
      - &lt;a href=&#34;http.md&#34;&gt;Http&lt;/a&gt;</i>
    <a href="#httptrap" title="Httptrap">Httptrap</a>: <i>
      - &lt;a href=&#34;httptrap.md&#34;&gt;Httptrap&lt;/a&gt;</i>
    <a href="#icmpping" title="IcmpPing">IcmpPing</a>: <i>
      - &lt;a href=&#34;icmpping.md&#34;&gt;IcmpPing&lt;/a&gt;</i>
    <a href="#jmx" title="Jmx">Jmx</a>: <i>
      - &lt;a href=&#34;jmx.md&#34;&gt;Jmx&lt;/a&gt;</i>
    <a href="#json" title="Json">Json</a>: <i>
      - &lt;a href=&#34;json.md&#34;&gt;Json&lt;/a&gt;</i>
    <a href="#memcached" title="Memcached">Memcached</a>: <i>
      - &lt;a href=&#34;memcached.md&#34;&gt;Memcached&lt;/a&gt;</i>
    <a href="#metric" title="Metric">Metric</a>: <i>
      - &lt;a href=&#34;metric.md&#34;&gt;Metric&lt;/a&gt;</i>
    <a href="#metricfilter" title="MetricFilter">MetricFilter</a>: <i>
      - &lt;a href=&#34;metricfilter.md&#34;&gt;MetricFilter&lt;/a&gt;</i>
    <a href="#mysql" title="Mysql">Mysql</a>: <i>
      - &lt;a href=&#34;mysql.md&#34;&gt;Mysql&lt;/a&gt;</i>
    <a href="#postgresql" title="Postgresql">Postgresql</a>: <i>
      - &lt;a href=&#34;postgresql.md&#34;&gt;Postgresql&lt;/a&gt;</i>
    <a href="#promtext" title="Promtext">Promtext</a>: <i>
      - &lt;a href=&#34;promtext.md&#34;&gt;Promtext&lt;/a&gt;</i>
    <a href="#redis" title="Redis">Redis</a>: <i>
      - &lt;a href=&#34;redis.md&#34;&gt;Redis&lt;/a&gt;</i>
    <a href="#snmp" title="Snmp">Snmp</a>: <i>
      - &lt;a href=&#34;snmp.md&#34;&gt;Snmp&lt;/a&gt;</i>
    <a href="#statsd" title="Statsd">Statsd</a>: <i>
      - &lt;a href=&#34;statsd.md&#34;&gt;Statsd&lt;/a&gt;</i>
    <a href="#tcp" title="Tcp">Tcp</a>: <i>
      - &lt;a href=&#34;tcp.md&#34;&gt;Tcp&lt;/a&gt;</i>
    <a href="#mbeanproperties" title="MbeanProperties">MbeanProperties</a>: <i>
      - &lt;a href=&#34;mbeanproperties.md&#34;&gt;MbeanProperties&lt;/a&gt;</i>
    <a href="#oid" title="Oid">Oid</a>: <i>
      - &lt;a href=&#34;oid.md&#34;&gt;Oid&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Active

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CheckByCollector

_Required_: No

_Type_: List of &lt;a href=&#34;checkbycollector.md&#34;&gt;CheckByCollector&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CheckId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Checks

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Created

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LastModified

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LastModifiedBy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricLimit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Notes

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Period

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReverseConnectUrls

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Target

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeout

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuids

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Caql

_Required_: No

_Type_: List of &lt;a href=&#34;caql.md&#34;&gt;Caql&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cloudwatch

_Required_: No

_Type_: List of &lt;a href=&#34;cloudwatch.md&#34;&gt;Cloudwatch&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Collector

_Required_: No

_Type_: List of &lt;a href=&#34;collector.md&#34;&gt;Collector&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Consul

_Required_: No

_Type_: List of &lt;a href=&#34;consul.md&#34;&gt;Consul&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dns

_Required_: No

_Type_: List of &lt;a href=&#34;dns.md&#34;&gt;Dns&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### External

_Required_: No

_Type_: List of &lt;a href=&#34;external.md&#34;&gt;External&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Http

_Required_: No

_Type_: List of &lt;a href=&#34;http.md&#34;&gt;Http&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Httptrap

_Required_: No

_Type_: List of &lt;a href=&#34;httptrap.md&#34;&gt;Httptrap&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IcmpPing

_Required_: No

_Type_: List of &lt;a href=&#34;icmpping.md&#34;&gt;IcmpPing&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Jmx

_Required_: No

_Type_: List of &lt;a href=&#34;jmx.md&#34;&gt;Jmx&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Json

_Required_: No

_Type_: List of &lt;a href=&#34;json.md&#34;&gt;Json&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Memcached

_Required_: No

_Type_: List of &lt;a href=&#34;memcached.md&#34;&gt;Memcached&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metric

_Required_: No

_Type_: List of &lt;a href=&#34;metric.md&#34;&gt;Metric&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricFilter

_Required_: No

_Type_: List of &lt;a href=&#34;metricfilter.md&#34;&gt;MetricFilter&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mysql

_Required_: No

_Type_: List of &lt;a href=&#34;mysql.md&#34;&gt;Mysql&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Postgresql

_Required_: No

_Type_: List of &lt;a href=&#34;postgresql.md&#34;&gt;Postgresql&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Promtext

_Required_: No

_Type_: List of &lt;a href=&#34;promtext.md&#34;&gt;Promtext&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Redis

_Required_: No

_Type_: List of &lt;a href=&#34;redis.md&#34;&gt;Redis&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Snmp

_Required_: No

_Type_: List of &lt;a href=&#34;snmp.md&#34;&gt;Snmp&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Statsd

_Required_: No

_Type_: List of &lt;a href=&#34;statsd.md&#34;&gt;Statsd&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tcp

_Required_: No

_Type_: List of &lt;a href=&#34;tcp.md&#34;&gt;Tcp&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MbeanProperties

_Required_: No

_Type_: List of &lt;a href=&#34;mbeanproperties.md&#34;&gt;MbeanProperties&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Oid

_Required_: No

_Type_: List of &lt;a href=&#34;oid.md&#34;&gt;Oid&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CheckByCollector

Returns the &lt;code&gt;CheckByCollector&lt;/code&gt; value.

#### CheckId

Returns the &lt;code&gt;CheckId&lt;/code&gt; value.

#### Checks

Returns the &lt;code&gt;Checks&lt;/code&gt; value.

#### Created

Returns the &lt;code&gt;Created&lt;/code&gt; value.

#### LastModified

Returns the &lt;code&gt;LastModified&lt;/code&gt; value.

#### LastModifiedBy

Returns the &lt;code&gt;LastModifiedBy&lt;/code&gt; value.

#### ReverseConnectUrls

Returns the &lt;code&gt;ReverseConnectUrls&lt;/code&gt; value.

#### Uuids

Returns the &lt;code&gt;Uuids&lt;/code&gt; value.

