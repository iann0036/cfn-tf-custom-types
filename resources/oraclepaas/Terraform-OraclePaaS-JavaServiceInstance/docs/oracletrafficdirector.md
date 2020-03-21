# Terraform::OraclePaaS::JavaServiceInstance OracleTrafficDirector

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#highavailability" title="HighAvailability">HighAvailability</a>" : <i>Boolean</i>,
    "<a href="#ipreservations" title="IpReservations">IpReservations</a>" : <i>[ String, ... ]</i>,
    "<a href="#loadbalancingpolicy" title="LoadBalancingPolicy">LoadBalancingPolicy</a>" : <i>String</i>,
    "<a href="#shape" title="Shape">Shape</a>" : <i>String</i>,
    "<a href="#admin" title="Admin">Admin</a>" : <i>[ &lt;a href=&#34;oracletrafficdirector-admin.md&#34;&gt;Admin&lt;/a&gt;, ... ]</i>,
    "<a href="#listener" title="Listener">Listener</a>" : <i>[ &lt;a href=&#34;oracletrafficdirector-listener.md&#34;&gt;Listener&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#highavailability" title="HighAvailability">HighAvailability</a>: <i>Boolean</i>
<a href="#ipreservations" title="IpReservations">IpReservations</a>: <i>
      - String</i>
<a href="#loadbalancingpolicy" title="LoadBalancingPolicy">LoadBalancingPolicy</a>: <i>String</i>
<a href="#shape" title="Shape">Shape</a>: <i>String</i>
<a href="#admin" title="Admin">Admin</a>: <i>
      - &lt;a href=&#34;oracletrafficdirector-admin.md&#34;&gt;Admin&lt;/a&gt;</i>
<a href="#listener" title="Listener">Listener</a>: <i>
      - &lt;a href=&#34;oracletrafficdirector-listener.md&#34;&gt;Listener&lt;/a&gt;</i>
</pre>

## Properties

#### HighAvailability

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpReservations

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancingPolicy

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Shape

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Admin

_Required_: No
_Type_: List of &lt;a href=&#34;oracletrafficdirector-admin.md&#34;&gt;Admin&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Listener

_Required_: No
_Type_: List of &lt;a href=&#34;oracletrafficdirector-listener.md&#34;&gt;Listener&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

