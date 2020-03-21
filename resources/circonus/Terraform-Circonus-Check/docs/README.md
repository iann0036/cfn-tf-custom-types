# Terraform::Circonus::Check

The ``circonus_check`` resource creates and manages a
[Circonus Check](https://login.circonus.com/resources/api/calls/check_bundle).

~> **NOTE regarding `circonus_check` vs a Circonus Check Bundle:** The
`circonus_check` resource is implemented in terms of a
[Circonus Check Bundle](https://login.circonus.com/resources/api/calls/check_bundle).
The `circonus_check` creates a higher-level abstraction over the implementation
of a Check Bundle.  As such, the naming and structure does not map 1:1 with the
underlying Circonus API.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Circonus::Check",
    "Properties" : {
        "<a href="#active" title="Active">Active</a>" : <i>Boolean</i>,
        "<a href="#metriclimit" title="MetricLimit">MetricLimit</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#notes" title="Notes">Notes</a>" : <i>String</i>,
        "<a href="#period" title="Period">Period</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#target" title="Target">Target</a>" : <i>String</i>,
        "<a href="#timeout" title="Timeout">Timeout</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#caql" title="Caql">Caql</a>" : <i>[ <a href="caql.md">Caql</a>, ... ]</i>,
        "<a href="#cloudwatch" title="Cloudwatch">Cloudwatch</a>" : <i>[ <a href="cloudwatch.md">Cloudwatch</a>, ... ]</i>,
        "<a href="#collector" title="Collector">Collector</a>" : <i>[ <a href="collector.md">Collector</a>, ... ]</i>,
        "<a href="#consul" title="Consul">Consul</a>" : <i>[ <a href="consul.md">Consul</a>, ... ]</i>,
        "<a href="#dns" title="Dns">Dns</a>" : <i>[ <a href="dns.md">Dns</a>, ... ]</i>,
        "<a href="#external" title="External">External</a>" : <i>[ <a href="external.md">External</a>, ... ]</i>,
        "<a href="#http" title="Http">Http</a>" : <i>[ <a href="http.md">Http</a>, ... ]</i>,
        "<a href="#httptrap" title="Httptrap">Httptrap</a>" : <i>[ <a href="httptrap.md">Httptrap</a>, ... ]</i>,
        "<a href="#icmpping" title="IcmpPing">IcmpPing</a>" : <i>[ <a href="icmpping.md">IcmpPing</a>, ... ]</i>,
        "<a href="#jmx" title="Jmx">Jmx</a>" : <i>[ <a href="jmx.md">Jmx</a>, ... ]</i>,
        "<a href="#json" title="Json">Json</a>" : <i>[ <a href="json.md">Json</a>, ... ]</i>,
        "<a href="#memcached" title="Memcached">Memcached</a>" : <i>[ <a href="memcached.md">Memcached</a>, ... ]</i>,
        "<a href="#metric" title="Metric">Metric</a>" : <i>[ <a href="metric.md">Metric</a>, ... ]</i>,
        "<a href="#metricfilter" title="MetricFilter">MetricFilter</a>" : <i>[ <a href="metricfilter.md">MetricFilter</a>, ... ]</i>,
        "<a href="#mysql" title="Mysql">Mysql</a>" : <i>[ <a href="mysql.md">Mysql</a>, ... ]</i>,
        "<a href="#postgresql" title="Postgresql">Postgresql</a>" : <i>[ <a href="postgresql.md">Postgresql</a>, ... ]</i>,
        "<a href="#promtext" title="Promtext">Promtext</a>" : <i>[ <a href="promtext.md">Promtext</a>, ... ]</i>,
        "<a href="#redis" title="Redis">Redis</a>" : <i>[ <a href="redis.md">Redis</a>, ... ]</i>,
        "<a href="#snmp" title="Snmp">Snmp</a>" : <i>[ <a href="snmp.md">Snmp</a>, ... ]</i>,
        "<a href="#statsd" title="Statsd">Statsd</a>" : <i>[ <a href="statsd.md">Statsd</a>, ... ]</i>,
        "<a href="#tcp" title="Tcp">Tcp</a>" : <i>[ <a href="tcp.md">Tcp</a>, ... ]</i>,
        "<a href="#mbeanproperties" title="MbeanProperties">MbeanProperties</a>" : <i>[ <a href="mbeanproperties.md">MbeanProperties</a>, ... ]</i>,
        "<a href="#oid" title="Oid">Oid</a>" : <i>[ <a href="oid.md">Oid</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Circonus::Check
Properties:
    <a href="#active" title="Active">Active</a>: <i>Boolean</i>
    <a href="#metriclimit" title="MetricLimit">MetricLimit</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#notes" title="Notes">Notes</a>: <i>String</i>
    <a href="#period" title="Period">Period</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#target" title="Target">Target</a>: <i>String</i>
    <a href="#timeout" title="Timeout">Timeout</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#caql" title="Caql">Caql</a>: <i>
      - <a href="caql.md">Caql</a></i>
    <a href="#cloudwatch" title="Cloudwatch">Cloudwatch</a>: <i>
      - <a href="cloudwatch.md">Cloudwatch</a></i>
    <a href="#collector" title="Collector">Collector</a>: <i>
      - <a href="collector.md">Collector</a></i>
    <a href="#consul" title="Consul">Consul</a>: <i>
      - <a href="consul.md">Consul</a></i>
    <a href="#dns" title="Dns">Dns</a>: <i>
      - <a href="dns.md">Dns</a></i>
    <a href="#external" title="External">External</a>: <i>
      - <a href="external.md">External</a></i>
    <a href="#http" title="Http">Http</a>: <i>
      - <a href="http.md">Http</a></i>
    <a href="#httptrap" title="Httptrap">Httptrap</a>: <i>
      - <a href="httptrap.md">Httptrap</a></i>
    <a href="#icmpping" title="IcmpPing">IcmpPing</a>: <i>
      - <a href="icmpping.md">IcmpPing</a></i>
    <a href="#jmx" title="Jmx">Jmx</a>: <i>
      - <a href="jmx.md">Jmx</a></i>
    <a href="#json" title="Json">Json</a>: <i>
      - <a href="json.md">Json</a></i>
    <a href="#memcached" title="Memcached">Memcached</a>: <i>
      - <a href="memcached.md">Memcached</a></i>
    <a href="#metric" title="Metric">Metric</a>: <i>
      - <a href="metric.md">Metric</a></i>
    <a href="#metricfilter" title="MetricFilter">MetricFilter</a>: <i>
      - <a href="metricfilter.md">MetricFilter</a></i>
    <a href="#mysql" title="Mysql">Mysql</a>: <i>
      - <a href="mysql.md">Mysql</a></i>
    <a href="#postgresql" title="Postgresql">Postgresql</a>: <i>
      - <a href="postgresql.md">Postgresql</a></i>
    <a href="#promtext" title="Promtext">Promtext</a>: <i>
      - <a href="promtext.md">Promtext</a></i>
    <a href="#redis" title="Redis">Redis</a>: <i>
      - <a href="redis.md">Redis</a></i>
    <a href="#snmp" title="Snmp">Snmp</a>: <i>
      - <a href="snmp.md">Snmp</a></i>
    <a href="#statsd" title="Statsd">Statsd</a>: <i>
      - <a href="statsd.md">Statsd</a></i>
    <a href="#tcp" title="Tcp">Tcp</a>: <i>
      - <a href="tcp.md">Tcp</a></i>
    <a href="#mbeanproperties" title="MbeanProperties">MbeanProperties</a>: <i>
      - <a href="mbeanproperties.md">MbeanProperties</a></i>
    <a href="#oid" title="Oid">Oid</a>: <i>
      - <a href="oid.md">Oid</a></i>
</pre>

## Properties

#### Active

Whether or not the check is enabled or not (default
`true`).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricLimit

Setting a metric limit will tell the Circonus
backend to periodically look at the check to see if there are additional
metrics the collector has seen that we should collect. It will not reactivate
metrics previously collected and then marked as inactive. Values are `0` to
disable, `-1` to enable all metrics or `N+` to collect up to the value `N`
(both `-1` and `N+` can not exceed other account restrictions).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the check that will be displayed in the web
interface.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Notes

Notes about this check.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Period

The period between each time the check is made in
seconds. Default is `"60s"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A list of tags assigned to this check.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Target

A string containing the location of the thing being
checked.  This value changes based on the check type.  For example, for an
`http` check type this would be the URL you're checking. For a DNS check it
would be the hostname you wanted to look up.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeout

A string representing the maximum number
of seconds this check should wait for a result.  Defaults to `"10s"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Caql

_Required_: No

_Type_: List of <a href="caql.md">Caql</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cloudwatch

_Required_: No

_Type_: List of <a href="cloudwatch.md">Cloudwatch</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Collector

_Required_: No

_Type_: List of <a href="collector.md">Collector</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Consul

_Required_: No

_Type_: List of <a href="consul.md">Consul</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dns

_Required_: No

_Type_: List of <a href="dns.md">Dns</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### External

_Required_: No

_Type_: List of <a href="external.md">External</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Http

_Required_: No

_Type_: List of <a href="http.md">Http</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Httptrap

_Required_: No

_Type_: List of <a href="httptrap.md">Httptrap</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IcmpPing

_Required_: No

_Type_: List of <a href="icmpping.md">IcmpPing</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Jmx

_Required_: No

_Type_: List of <a href="jmx.md">Jmx</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Json

_Required_: No

_Type_: List of <a href="json.md">Json</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Memcached

_Required_: No

_Type_: List of <a href="memcached.md">Memcached</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metric

_Required_: No

_Type_: List of <a href="metric.md">Metric</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricFilter

_Required_: No

_Type_: List of <a href="metricfilter.md">MetricFilter</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mysql

_Required_: No

_Type_: List of <a href="mysql.md">Mysql</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Postgresql

_Required_: No

_Type_: List of <a href="postgresql.md">Postgresql</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Promtext

_Required_: No

_Type_: List of <a href="promtext.md">Promtext</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Redis

_Required_: No

_Type_: List of <a href="redis.md">Redis</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Snmp

_Required_: No

_Type_: List of <a href="snmp.md">Snmp</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Statsd

_Required_: No

_Type_: List of <a href="statsd.md">Statsd</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tcp

_Required_: No

_Type_: List of <a href="tcp.md">Tcp</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MbeanProperties

_Required_: No

_Type_: List of <a href="mbeanproperties.md">MbeanProperties</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Oid

_Required_: No

_Type_: List of <a href="oid.md">Oid</a>

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

Returns the <code>CheckByCollector</code> value.

#### CheckId

Returns the <code>CheckId</code> value.

#### Checks

Returns the <code>Checks</code> value.

#### Created

Returns the <code>Created</code> value.

#### LastModified

Returns the <code>LastModified</code> value.

#### LastModifiedBy

Returns the <code>LastModifiedBy</code> value.

#### ReverseConnectUrls

Returns the <code>ReverseConnectUrls</code> value.

#### Uuids

Returns the <code>Uuids</code> value.

